<template>
  <div class="header">
    <div class="header-left">
      <div class="logo">Group AM final project</div>
    </div>
    <div class="header-right">
      <el-menu
        :default-active="activeMenu"
        mode="horizontal"
        @select="handleMenuSelect"
        background-color="#363535"
        text-color="#cccccc"
        active-text-color="#E9DFD5"
      >
        <el-menu-item index="home">
          Home
        </el-menu-item>
        <!-- <el-menu-item index="overview">
          Recommended scenic routes  
        </el-menu-item> -->
        <el-menu-item index="scenicAreaData">
          Beijing Scenic Area Data
        </el-menu-item>
        <!-- <el-menu-item index="sport">
          Sports Products Section
        </el-menu-item> -->
      </el-menu>
    </div>
  </div>
</template>

<script setup>
import { FullScreen } from "@element-plus/icons-vue";
import { useRouter, useRoute } from "vue-router";
import { ref, watch } from "vue";

const router = useRouter();
const route = useRoute();
const activeMenu = ref("overview");

watch(
  () => route.path,
  (newPath) => {
    // 处理首页重定向情况
    if (newPath === '/') {
      activeMenu.value = "home";
      return;
    }

    // 从路径中提取页面名称（去除开头的斜杠）
    const pathName = newPath.substring(1);
    // 确保路径名有效后再更新
    if (pathName && ['home','scenicAreaData'].includes(pathName)) {
      activeMenu.value = pathName;
    }
  },
  { immediate: true }
);

const toggleFullscreen = () => {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
};

const logout = () => {
  router.push("/login");
};

const handleMenuSelect = (index) => {
  router.push(`/${index}`);
};
</script>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 56px;
  padding: 0 24px;
  box-sizing: border-box;
  background-color: #363535;
  box-shadow: 2px 0 10px 0 rgba(15, 88, 255, 0.05);
  border-bottom: 1px solid #363535;

  .header-left {
    display: flex;
    align-items: center;
    
    .logo {
      font-size: 18px;
      font-weight: bold;
      color: #E9DFD5;
      margin-right: 30px;
    }
  }

  .header-right {
    display: flex;
    align-items: center;
    gap: 20px;
    width: 350px;

    
    ::v-deep(.el-menu.el-menu--horizontal) {
      border-bottom: none;
      background-color: #363535 !important;
      width: 100%; /* 设置宽度为100% */
      
      .el-menu-item {
        height: 56px;
        line-height: 56px;
        
        &.is-active {
          border-bottom: 2px solid #E9DFD5;
          color: #E9DFD5 !important;
        }
        
        &:not(.is-active) {
          color: #cccccc !important; /* 淡灰色 */
          
          &:hover {
            color: #ffffff !important; /* 鼠标悬停时变为白色 */
          }
        }
      }
    }
  }
}
</style>