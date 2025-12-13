import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": "/src",
    },
  },
  base: "/", // 根据环境动态设置基础路径
  server: {
    proxy: {
      "/api": {
        // target: "xxx", // 代理到后端服务
        target: "http://103.85.23.75", // 代理到后端服务

        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/api/, ''), // 重写路径
      },
    },
  },
  build: {
    outDir: "dist", // 输出目录
    assetsDir: "assets", // 静态资源目录
  },
  optimizeDeps: {
    include: ["vue", "element-plus"],
  },
});
