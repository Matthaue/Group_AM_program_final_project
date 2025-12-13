<template>
  <div ref="chartContainer" class="pictorial-bar-container"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue';
import * as echarts from 'echarts';

const props = defineProps({
  // 图表数据 { female: number, male: number }
  data: {
    type: Object,
    required: true,
    default: () => ({ female: 0, male: 0 })
  },
  // 图表高度
  height: {
    type: String,
    default: '350px'
  },
  // 图表标题
  title: {
    type: String,
    default: 'Gender Distribution'
  }
});

const chartContainer = ref(null);
let chartInstance = null;

// 简化的SVG图标路径
const femaleSymbol = 'path://M12,2C13.1,2 14,2.9 14,4C14,5.1 13.1,6 12,6C10.9,6 10,5.1 10,4C10,2.9 10.9,2 12,2ZM21,9V7L15,5.5V7H9V5.5L3,7V9L9,10.5V12.5L3,14V16L9,14.5V21H15V14.5L21,16V14L15,12.5V10.5L21,9Z';
const maleSymbol = 'path://M12,2C13.1,2 14,2.9 14,4C14,5.1 13.1,6 12,6C10.9,6 10,5.1 10,4C10,2.9 10.9,2 12,2ZM10.5,7H13.5V10H10.5V7ZM10.5,11H13.5V21H10.5V11Z';

// 初始化图表
const initChart = () => {
  if (!chartContainer.value) {
    console.warn('图表容器未找到');
    return;
  }
  
  // 销毁旧实例
  if (chartInstance) {
    chartInstance.dispose();
    chartInstance = null;
  }
  
  // 设置容器尺寸
  chartContainer.value.style.height = props.height;
  chartContainer.value.style.width = '100%';
  
  try {
    chartInstance = echarts.init(chartContainer.value);
    
    const option = {
      tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'shadow' },
        formatter: function (params) {
          let result = '';
          params.forEach(param => {
            if (param.value !== '-') {
              result = `${param.seriesName}: ${param.value}%`;
            }
          });
          return result;
        }
      },
      legend: {
        show: true,
        top: '0%',
        textStyle: { color: '#606266' }
      },
      grid: {
        left: '15%',
        right: '10%',
        bottom: '10%',
        top: '15%',
        containLabel: true
      },
      xAxis: {
        type: 'value',
        name: 'Percentage (%)',
        max: 100,
        nameTextStyle: { color: '#606266' },
        axisLabel: { 
          color: '#606266', 
          fontSize: 12,
          formatter: '{value}%'
        },
        axisLine: { lineStyle: { color: '#ddd' } },
        splitLine: { lineStyle: { color: '#eee' } }
      },
      yAxis: {
        type: 'category',
        data: ['Female', 'Male'],
        axisLabel: { 
          color: '#606266', 
          fontSize: 14
        },
        axisLine: { lineStyle: { color: '#ddd' } }
      },
      series: [
        {
          name: 'Female',
          type: 'pictorialBar',
          data: [props.data.female, '-'],
          symbol: femaleSymbol,
          symbolSize: [20, 20],
          symbolRepeat: true,
          symbolMargin: 2,
          symbolBoundingData: 100,
          itemStyle: { color: '#d37a90' },
          label: {
            show: true,
            position: 'right',
            formatter: function (params) {
              return params.value !== '-' ? `${params.value}%` : '';
            },
            textStyle: { 
              color: '#333', 
              fontSize: 14, 
              fontWeight: 'bold' 
            }
          },
          z: 2
        },
        {
          name: 'Male',
          type: 'pictorialBar',
          data: ['-', props.data.male],
          symbol: maleSymbol,
          symbolSize: [20, 20],
          symbolRepeat: true,
          symbolMargin: 2,
          symbolBoundingData: 100,
          itemStyle: { color: '#5470c6' },
          label: {
            show: true,
            position: 'right',
            formatter: function (params) {
              return params.value !== '-' ? `${params.value}%` : '';
            },
            textStyle: { 
              color: '#333', 
              fontSize: 14, 
              fontWeight: 'bold' 
            }
          },
          z: 1
        }
      ],
      animation: true,
      animationDuration: 1000
    };
    
    chartInstance.setOption(option);
    
    // 响应式调整
    const handleResize = () => {
      if (chartInstance) {
        chartInstance.resize();
      }
    };
    
    window.addEventListener('resize', handleResize);
    
  } catch (error) {
    console.error('图表初始化失败:', error);
    initFallbackChart();
  }
};

// 备用方案：普通柱状图
const initFallbackChart = () => {
  if (!chartContainer.value || !chartInstance) return;
  
  const option = {
    tooltip: {
      trigger: 'axis',
      formatter: '{b}: {c}%'
    },
    xAxis: {
      type: 'category',
      data: ['Female', 'Male']
    },
    yAxis: {
      type: 'value',
      max: 100,
      axisLabel: {
        formatter: '{value}%'
      }
    },
    series: [{
      data: [props.data.female, props.data.male],
      type: 'bar',
      itemStyle: {
        color: function(params) {
          return params.dataIndex === 0 ? '#d37a90' : '#5470c6';
        }
      },
      label: {
        show: true,
        position: 'top',
        formatter: '{c}%'
      }
    }]
  };
  
  chartInstance.setOption(option);
};

// 监听数据变化
watch(() => props.data, () => {
  nextTick(() => {
    initChart();
  });
}, { deep: true });

onMounted(() => {
  nextTick(() => {
    initChart();
  });
});

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.dispose();
    chartInstance = null;
  }
});
</script>

<style scoped>
.pictorial-bar-container {
  width: 100%;
  background-color: white;
  border-radius: 8px;
}
</style>