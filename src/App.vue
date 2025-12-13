<script setup>
import Header from "@/components/Header.vue";
import Layout from "@/components/Layout.vue";
import { useRoute } from 'vue-router';
import { computed } from 'vue';

const route = useRoute();
const showLayout = computed(() => route.meta.hideLayout ?? false);
console.log("showLayout:", showLayout);
</script>

<template>
  <div class="App">
    <Header v-if="!showLayout" />
    <div class="content">
      <Layout v-if="!showLayout" class="layout" />
      <div class="main" :class="{ 'full-width': showLayout }">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.App {
  height: 100vh;
  .content {
    height: calc(100vh - 56px);
    display: flex;
    .layout {
      flex: 0 0 0px; /* 确保没有宽度 */
      width: 0px !important;
    }
    .main {
      flex: 1;
      padding: 0px;
      background: #f7f8fa;
      &.full-width {
        height: 100vh;
        padding: 0;
      }
    }
  }
}
</style>