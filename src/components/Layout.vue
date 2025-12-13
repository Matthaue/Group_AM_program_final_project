<template>
  <!-- <el-container class="layout">
    <el-aside class="sider">
      <el-menu
        class="el-menu-vertical"
        :default-active="activeMenu"
        :unique-opened="false"
        @select="handleMenuClick"
      >
        <el-menu-item index="overview">
          <el-icon><el-icon-sport /></el-icon> -->
          <!-- 核心财务指标 -->
          <!-- <span> Core financial indicators</span>   
        </el-menu-item>
         <el-menu-item index="scenicAreaData">
          <el-icon><el-icon-sport /></el-icon> -->
          <!-- 业务板块 -->
          <!-- <span>Business Segment</span>
        </el-menu-item>
         <el-menu-item index="sport">
          <el-icon><el-icon-sport /></el-icon>
          <span> 系统设置</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
  </el-container> -->
</template>

<script>
import { ref , watch } from "vue";
import { useRouter, useRoute  } from "vue-router";
import { Menu as ElIconMenu, Setting as ElIconSetting } from '@element-plus/icons-vue'

export default {
  components: {
    ElIconMenu,
    ElIconSetting
  },
  setup() {
    const router = useRouter();
    const route = useRoute();
    const activeMenu = ref("overview");

    // const handleMenuClick = (index) => {
    //   router.push(`/${index}`);
    // };
    // 监听路由变化，同步更新菜单激活状态
    watch(
      () => route.path,
      (newPath) => {
        // 处理首页重定向情况
        if (newPath === '/') {
          activeMenu.value = "overview";
          return;
        }
    
        // 从路径中提取页面名称（去除开头的斜杠）
        const pathName = newPath.substring(1);
        // 确保路径名有效后再更新
        if (pathName && ['overview', 'scenicAreaData'].includes(pathName)) {
          activeMenu.value = pathName;
        }
     },    
     { immediate: true }
    );

    const handleMenuClick = (index) => {
      router.push(`/${index}`);
    };

    return {
      activeMenu,
      handleMenuClick
    };
  }
};
</script>

<style scoped lang="scss">
.layout {
  height: 100%;
}

.sider {
  width: 201px !important;
  background: #fff;
  box-shadow: 2px 0 8px 0 rgba(29, 35, 41, 0.05);
}

.el-menu-vertical {
  border-right: none;
}

.el-menu-item {
  width: 100% !important;
  margin: 0 !important;
  border-radius: 0 !important;
  height: 48px !important;
  line-height: 48px !important;
  transition: none !important;

  &:hover {
    background: transparent !important;
    color: inherit !important;
  }
}

.el-menu-item.is-active {
  background-color: #f0f7ff !important;
  border-right: 4px solid #E9DFD5 !important;
  color: #E9DFD5 !important;
  font-weight: 500;

  .el-icon {
    color: #E9DFD5 !important;
  }
}

.el-menu-item a {
  color: #595959 !important;
}

.el-menu-item.is-active a {
  color: #E9DFD5 !important;
}

.el-sub-menu__title {
  transition: none !important;

  &:hover {
    background: transparent !important;
    color: inherit !important;
  }
}

.el-menu--inline {
  background: #fafafa !important;
}

.el-sub-menu.is-active .el-sub-menu__title {
  color: #E9DFD5 !important;

  .el-icon {
    color: #E9DFD5 !important;
  }
}

.el-icon {
  font-size: 16px !important;
  margin-right: 10px !important;
  color: #595959 !important;
}
</style>