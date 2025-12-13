import axios from "axios";
import { ElMessage } from "element-plus";
import router from "@/router";

const service = axios.create({
  baseURL: '/api',
  timeout: 15000,
  headers: {
    "Content-Type": "application/json",
  },
  responseType: 'arraybuffer'
});

// 请求拦截器
service.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers["token"] = token;
    }
    
    if (config.url?.includes('download') || config.params?.isDownload) {
      config.responseType = 'blob';
    }
    
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
service.interceptors.response.use(
  (response) => {
    if (response.config.responseType === 'blob' || 
        response.headers['content-type']?.includes('application/octet-stream')) {
      return handleFileResponse(response);
    }
    
    try {
      const responseText = arrayBufferToString(response.data);
      const res = JSON.parse(responseText);
      
      if (res.code === 0) {
        return res;
      }
      
      const message = res.message || "请求失败";
      ElMessage.error(message);
      
      if (res.status === 501) {
        handleUnauthorized();
      }
      
      return Promise.reject(new Error(message));
    } catch (e) {
      return response.data;
    }
  },
  (error) => {
    if (error.response) {
      if (error.config.responseType === 'blob' || 
          error.response.headers['content-type']?.includes('application/octet-stream')) {
        return parseBlobError(error);
      }
      
      switch (error.response.status) {
        case 401:
        case 501:
          handleUnauthorized();
          break;
        case 404:
          ElMessage.error("请求资源不存在");
          break;
        case 500:
          ElMessage.error("服务器内部错误");
          break;
        default:
          ElMessage.error(error.response.data?.message || "请求失败");
      }
    } else if (error.request) {
      ElMessage.error("网络错误，请检查您的网络连接");
    } else {
      ElMessage.error(error.message || "请求失败");
    }
    
    return Promise.reject(error);
  }
);

// 处理文件下载响应（兼容移动设备）
function handleFileResponse(response) {
  return new Promise((resolve, reject) => {
    const contentDisposition = response.headers['content-disposition'];
    let filename = 'download';
    
    if (contentDisposition) {
      const match = contentDisposition.match(/filename=(.*)/);
      if (match) {
        filename = match[1];
        if (filename.startsWith("UTF-8''")) {
          filename = decodeURIComponent(filename.replace("UTF-8''", ""));
        } else {
          filename = filename.replace(/"/g, '');
        }
      }
    }
    
    try {
      const blob = new Blob([response.data]);
      const url = URL.createObjectURL(blob);
      
      // 创建隐藏的iframe来触发下载
      const iframe = document.createElement('iframe');
      iframe.style.display = 'none';
      iframe.src = url;
      document.body.appendChild(iframe);
      
      // 对于移动设备，可能需要用户手动操作触发下载
      // 这里返回下载URL让调用方决定如何处理
      resolve({ 
        success: true, 
        filename,
        blobUrl: url,
        blobData: blob
      });
      
      // 延迟清理，确保下载开始
      setTimeout(() => {
        document.body.removeChild(iframe);
        URL.revokeObjectURL(url);
      }, 10000);
    } catch (e) {
      reject(new Error("文件下载失败"));
    }
  });
}

// 解析blob类型的错误响应
function parseBlobError(error) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const errorText = reader.result;
        const errorData = JSON.parse(errorText);
        ElMessage.error(errorData.message || "下载失败");
        reject(new Error(errorData.message || "下载失败"));
      } catch (e) {
        ElMessage.error("下载文件失败");
        reject(new Error("下载文件失败"));
      }
    };
    reader.readAsText(error.response.data);
  });
}

function arrayBufferToString(buffer) {
  const decoder = new TextDecoder('utf-8');
  return decoder.decode(buffer);
}

function handleUnauthorized() {
  ElMessage.error("登录已过期，请重新登录");
  localStorage.clear();
  setTimeout(() => {
    router.push("/login");
  }, 1000);
}

export default service;