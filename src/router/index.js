
import { createRouter, createWebHistory } from "vue-router";
import login from "../pages/login.vue";
// import overview from "../pages/overview/overview.vue";
import scenicAreaData from "../pages/scenicAreaData/scenicAreaData.vue";
// import sport from "../pages/sport/sport.vue";
import home from "../pages/home/home.vue";

const routes = [
  {
    path: "/",
    redirect: "/home",
  },
  { path: "/login", component: login, meta: { hideLayout: true } },
  { path: "/home", component: home },
  // { path: "/overview", component: overview },
  { path: "/scenicAreaData", component: scenicAreaData },
  // { path: "/sport", component: sport },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 添加路由错误处理
router.onError((error) => {
  console.error("路由错误:", error);
});

export default router;