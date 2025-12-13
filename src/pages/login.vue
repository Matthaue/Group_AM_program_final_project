<template>
  <div class="login-container">
    <div class="login-box">
      <div class="login-header">
        <h2>欢迎登录系统</h2>
      </div>

      <el-form
        ref="loginFormRef"
        :model="loginForm"
        :rules="loginRules"
        class="login-form"
      >
        <el-form-item prop="username">
          <el-input
            v-model="loginForm.username"
            placeholder="用户名"
            prefix-icon="User"
            clearable
            style="height: 34px"
            @keyup.enter.native="handleLogin"
          />
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="loginForm.password"
            type="password"
            placeholder="密码"
            prefix-icon="Lock"
            show-password
            clearable
            style="height: 34px;margin-top: 20px;"
            @keyup.enter.native="handleLogin"
          />
        </el-form-item>

        <el-form-item>
          <el-button
            type="primary"
            :loading="loading"
            class="login-button"
            @click="handleLogin"
          >
            登录
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { api } from "@/api/api";
// import { useUserStore } from "@/store/user";

export default {
  setup() {
    // const userStore = useUserStore();
    const router = useRouter();
    const loginFormRef = ref(null);
    const loading = ref(false);

    const loginForm = reactive({
      username: "",
      password: "",
      remember: false,
    });

    const loginRules = {
      username: [
        { required: true, trigger: "blur", message: "请输入用户名" },
      ],
      password: [
        { required: true, trigger: "blur", message: "请输入密码" },
      ],
    };

    const handleLogin = async () => {
      if (!loginFormRef.value) return;

      try {
        await loginFormRef.value.validate();
        loading.value = true;
        const params = {
          user: {
            fuName: loginForm.username,
            fuPwd: loginForm.password,
          },
        };
        // api
        //   .login(params)
        //   .then((res) => {
        //     localStorage.setItem("token", res.data.token);
        //     localStorage.setItem("user", JSON.stringify(res.data.user));
        //     userStore.updateUserInfo(res.data.user);

        //     const menuList = res.data.menuList;
        //     localStorage.setItem("menu", JSON.stringify(menuList));

        //     ElMessage({
        //       message: "登录成功",
        //       type: "success",
        //       duration: 1000,
        //       showClose: false,
        //       onClose: () => {
        //         router.push("/home");
        //       },
        //     });
        //   })
        //   .finally(() => {
        //     loading.value = false;
        //   });
      } catch (error) {
        console.error("登录验证失败", error);
        loading.value = false;
      }
    };

    const handleGlobalEnter = (e) => {
      if (e.key === "Enter" && !(e.target instanceof HTMLInputElement)) {
        handleLogin();
      }
    };

    onMounted(() => {
      document.addEventListener("keydown", handleGlobalEnter);
    });

    onUnmounted(() => {
      document.removeEventListener("keydown", handleGlobalEnter);
    });

    return {
      loginFormRef,
      loading,
      loginForm,
      loginRules,
      handleLogin,
    };
  },
};
</script>

<style scoped>
.login-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  overflow: hidden;
    background: url("../assets/login.jpg") no-repeat center center;
  background-size: cover;
}

.login-container::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;

  filter: blur(4px);
  z-index: -1;
  transform: scale(1.05);
}

.login-box {
  width: 350px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
  position: relative;
  z-index: 1;
}

.login-header {
  text-align: center;
  margin-bottom: 30px;
}

.login-header h2 {
  font-size: 20px;
  color: #303133;
  margin: 0;
}

.login-form {
  margin-top: 10px;
}

.login-form :deep(.el-form-item) {
  margin-bottom: 10px;
}

.login-button {
  width: 100%;
  margin-top: 15px;
}
</style>