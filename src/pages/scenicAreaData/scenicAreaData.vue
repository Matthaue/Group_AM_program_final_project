<template>
  <div class="team-knowledge">
    <div class="page-header">
      <div class="logo-container">
        <img src="../../figure/gugong.jpg" alt="Gugong" style="width: 100%; height: 100%;">
        <div class="logo-text">Beijing Scenic Area Data</div>
      </div>
    </div>

    <!-- 游客数量堆叠柱状图 -->
    <el-card class="document-list">
      <div class="chart-container">
        <div ref="stackedBarChart" class="stacked-bar-chart"></div>
      </div>
    </el-card>

    <el-card class="document-list">
      <!-- 人均消费堆叠柱状图 -->
      <div class="chart-container">
        <div ref="consumptionChart" class="consumption-chart"></div>
      </div>
    </el-card>

    <!-- 营收水平柱状图 -->
    <el-card class="document-list">
      <div class="chart-container">
        <div ref="revenueChart" class="revenue-chart"></div>
      </div>
    </el-card>

    <!-- 推荐路线 -->
    <el-card class="document-list">
      <!-- <div class="chart-container">
        <div ref="routeChart" class="route-chart"></div>
      </div> -->

      <!-- 路线详情展示 -->
      <div class="route-info">
        <div class="route-summary">
          <div class="summary-item">
            <h3>Total Time</h3>
            <p>{{ routeData.total_time_min }} min</p>
          </div>
          <div class="summary-item">
            <h3>Total Distance</h3>
            <p>{{ routeData.total_distance_km }} km.</p>
          </div>
          <div class="summary-item">
            <h3>Total Taxi Fare</h3>
            <p>¥{{ routeData.total_price_yuan }} </p>
          </div>
        </div>

        <div class="route-steps">
          <div class="step-item" v-for="(step, index) in routeData.steps" :key="index">
            <div class="step-header">
              <div class="step-number">{{ index + 1 }}</div>
              <div class="step-title">{{ step.from }} → {{ step.to }}</div>
            </div>
            <div class="step-details">
              <div class="detail-item">
                <h4>Public Transportation Routes</h4>
                <p><span class="transport-icon">M</span> {{ step.public_transport_route }}</p>
              </div>
              <div class="detail-item">
                <h4>Distance</h4>
                <p>{{ step.distance_km }} km.</p>
              </div>
              <div class="detail-item">
                <h4>Time</h4>
                <p>{{ step.time_min }} min</p>
              </div>
              <div class="detail-item">
                <h4>Taxi Fare</h4>
                <p>¥{{ step.taxi_price_yuan }} </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from "vue";
import * as echarts from 'echarts';

// 堆叠柱状图实例
const stackedBarChart = ref(null);
let chartInstance = null;

// 人均消费柱状图实例
const consumptionChart = ref(null);
let consumptionChartInstance = null;

// 营收柱状图实例
const revenueChart = ref(null);
let revenueChartInstance = null;

// 景点数据
const scenicSpotData = [
  {
    name: 'The Forbidden City',
    lowSeason: 2.9,
    peakSeason: 4.8
  },
  {
    name: 'Temple of Heaven',
    lowSeason: 1.75,
    peakSeason: 3.5
  },
  {
    name: 'the Summer Palace',
    lowSeason: 2.5,
    peakSeason: 5.5
  },
  {
    name: 'Yuanmingyuan Ruins Park',
    lowSeason: 1.75,
    peakSeason: 2.75
  },
  {
    name: 'Badaling Great Wall',
    lowSeason: 2.21,
    peakSeason: 4.74
  },
  {
    name: 'Beihai Park',
    lowSeason: 1.03,
    peakSeason: 1.64
  },
  {
    name: 'Lama Temple',
    lowSeason: 1.67,
    peakSeason: 4.09
  },
  {
    name: 'National Museum of China',
    lowSeason: 2.02,
    peakSeason: 2.5
  },
  {
    name: 'Bird\'s Nest (National Stadium)',
    lowSeason: 0.57,
    peakSeason: 1.09,
    specialNote: 'Concerts and events attract an average of 30000 to 50000 attendees per day'
  },
  {
    name: 'Water Cube',
    lowSeason: 0.32,
    peakSeason: 0.8
  },
  {
    name: 'Xiangshan Park',
    lowSeason: 0.15,
    peakSeason: 1.4,
    specialNote: 'During the red leaf period (late October to mid November), there are an average of 50000 people per day'
  },
  {
    name: 'Nanluoguxiang',
    lowSeason: 3.2,
    peakSeason: 6.5
  },
  {
    name: 'Shichahai',
    lowSeason: 7.5,
    peakSeason: 22
  },
  {
    name: 'Military Museum',
    lowSeason: 1.5,
    peakSeason: 2.461
  },
  {
    name: '798 Art District',
    lowSeason: 1,
    peakSeason: 6
  },
  {
    name: 'Universal Studios Beijing',
    lowSeason: 1.5,
    peakSeason: 3.9
  }
];

// 人均消费数据
const consumptionData = [
  { name: 'The Forbidden City', min: 140, max: 200 },
  { name: 'Temple of Heaven', min: 80, max: 120 },
  { name: 'the Summer Palace', min: 100, max: 150 },
  { name: 'Yuanmingyuan Ruins Park', min: 60, max: 100 },
  { name: 'Badaling Great Wall', min: 40, max: 145 },
  { name: 'Beihai Park', min: 5, max: 20 },
  { name: 'Lama Temple', min: 25, max: 500 },
  { name: 'National Museum of China', min: 0, max: 50 },
  { name: 'Bird\'s Nest (National Stadium)', min: 50, max: 100 },
  { name: 'Water Cube', min: 30, max: 260 },
  { name: 'Xiangshan Park', min: 50, max: 80 },
  { name: 'Nanluoguxiang', min: 100, max: 150 },
  { name: 'Shichahai', min: 50, max: 320 },
  { name: 'Military Museum', min: 0, max: 50 },
  { name: '798 Art District', min: 0, max: 200 },
  { name: 'Universal Studios Beijing', min: 1000, max: 2000 }
];

// 营收数据
const revenueData = [
  { name: 'The Forbidden City', lowSeason: [46, 52], peakSeason: [73, 79] },
  { name: 'Temple of Heaven', lowSeason: [1.8, 2.4], peakSeason: [4.5, 5.4] },
  { name: 'the Summer Palace', lowSeason: [3, 4.5], peakSeason: [9, 10.5] },
  { name: 'Yuanmingyuan Ruins Park', lowSeason: [0.9, 1.35], peakSeason: [2.36, 3.15] },
  { name: 'Badaling Great Wall', lowSeason: [0.775, 0.775], peakSeason: [2.325, 2.325] },
  { name: 'Beihai Park', lowSeason: [0.645, 0.645], peakSeason: [1.533, 1.533] },
  { name: 'Lama Temple', lowSeason: [0.24, 0.24], peakSeason: [0.56, 0.56] },
  { name: 'National Museum of China', lowSeason: [0.96, 0.96], peakSeason: [1.44, 1.44] },
  { name: 'Bird\'s Nest (National Stadium)', lowSeason: [0.75, 0.75], peakSeason: [1.75, 1.75] },
  { name: 'Water Cube', lowSeason: [0.37, 0.37], peakSeason: [0.87, 0.87] },
  { name: 'Xiangshan Park', lowSeason: [0.75, 0.75], peakSeason: [2.24, 2.24] },
  { name: 'Nanluoguxiang', lowSeason: [1.05, 1.05], peakSeason: [1.95, 1.95] },
  { name: 'Military Museum', lowSeason: [0, 0], peakSeason: [0.002, 0.002] },
  { name: '798 Art District', lowSeason: [0.28, 0.28], peakSeason: [0.8, 0.8] },
  { name: 'Universal Studios Beijing', lowSeason: [10, 10], peakSeason: [23.77, 23.77] }
];

// 初始化游客数量堆叠柱状图
const initStackedBarChart = () => {
  setTimeout(() => {
    if (!stackedBarChart.value) {
      console.error('Stacked bar chart DOM not found');
      return;
    }

    const dom = stackedBarChart.value;
    if (dom.clientWidth === 0 || dom.clientHeight === 0) {
      setTimeout(initStackedBarChart, 100);
      return;
    }

    if (chartInstance) {
      chartInstance.dispose();
    }

    chartInstance = echarts.init(dom);

    const option = {
      title: {
        text: 'Statistics on the number of tourists to major tourist attractions in Beijing (10000 people/day)',
        left: 'center',
        textStyle: {
          fontSize: 18,
          fontWeight: 'bold',
          color: '#333'
        }
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        },
        formatter: function (params) {
          let result = params[0].name + '<br/>';
          params.forEach(param => {
            const value = param.value.toFixed(2);
            const seriesName = param.seriesName;
            const color = param.color;

            result += `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${color};"></span>`;
            result += `${seriesName}: ${value} ten thousand person-times<br/>`;

            const spotData = scenicSpotData.find(item => item.name === param.name);
            if (spotData && spotData.specialNote && seriesName === 'off-season') {
              result += `<span style="color:#ff6b6b;font-size:12px;">※ ${spotData.specialNote}</span><br/>`;
            }
          });
          return result;
        }
      },
      legend: {
        data: ['off-season', 'peak season'],
        top: '7%',
        textStyle: {
          fontSize: 14
        }
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '10%',
        top: '15%',
        containLabel: true
      },
      xAxis: {
        type: 'category',
        data: scenicSpotData.map(item => item.name),
        axisLabel: {
          rotate: 45,
          fontSize: 10,
          interval: 0
        },
        axisTick: {
          alignWithLabel: true
        }
      },
      yAxis: {
        type: 'value',
        name: '10000 people/day',
        nameTextStyle: {
          fontSize: 12
        },
        axisLabel: {
          fontSize: 11
        }
      },
      series: [
        {
          name: 'off-season',
          type: 'bar',
          stack: 'total',
          data: scenicSpotData.map(item => item.lowSeason),
          itemStyle: {
            color: '#5470c6'
          },
          label: {
            show: true,
            position: 'inside',
            formatter: function (params) {
              return params.value.toFixed(1);
            },
            fontSize: 10,
            color: '#fff'
          }
        },
        {
          name: 'peak season',
          type: 'bar',
          stack: 'total',
          data: scenicSpotData.map(item => item.peakSeason),
          itemStyle: {
            color: '#91cc75'
          },
          label: {
            show: true,
            position: 'inside',
            formatter: function (params) {
              return params.value.toFixed(1);
            },
            fontSize: 10,
            color: '#fff'
          }
        }
      ],
      dataZoom: [
        {
          type: 'inside',
          start: 0,
          end: 40
        },
        {
          type: 'slider',
          start: 0,
          end: 40,
          bottom: '2%',
          height: 20
        }
      ]
    };

    chartInstance.setOption(option);

    window.addEventListener('resize', () => {
      if (chartInstance) {
        chartInstance.resize();
      }
    });
  }, 100);
};

// 初始化人均消费堆叠柱状图
const initConsumptionChart = () => {
  setTimeout(() => {
    if (!consumptionChart.value) {
      console.error('Consumption chart DOM not found');
      return;
    }

    const dom = consumptionChart.value;
    if (dom.clientWidth === 0 || dom.clientHeight === 0) {
      setTimeout(initConsumptionChart, 100);
      return;
    }

    if (consumptionChartInstance) {
      consumptionChartInstance.dispose();
    }

    consumptionChartInstance = echarts.init(dom);

    const option = {
      title: {
        text: 'Average Consumption per Person at Major Tourist Attractions in Beijing (RMB)',
        left: 'center',
        textStyle: {
          fontSize: 18,
          fontWeight: 'bold',
          color: '#333'
        }
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        },
        formatter: function (params) {
          let result = params[0].name + '<br/>';
          params.forEach(param => {
            const value = param.value;
            const seriesName = param.seriesName;
            const color = param.color;

            result += `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${color};"></span>`;
            result += `${seriesName}: ${value} RMB<br/>`;
          });

          const data = consumptionData.find(item => item.name === params[0].name);
          if (data) {
            result += `Total Range: ${data.min} - ${data.max} RMB`;
          }

          return result;
        }
      },
      legend: {
        data: ['Minimum Consumption', 'Additional Consumption'],
        top: '7%',
        textStyle: {
          fontSize: 14
        }
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '10%',
        top: '15%',
        containLabel: true
      },
      xAxis: {
        type: 'category',
        data: consumptionData.map(item => item.name),
        axisLabel: {
          rotate: 45,
          fontSize: 10,
          interval: 0
        },
        axisTick: {
          alignWithLabel: true
        }
      },
      yAxis: {
        type: 'value',
        name: 'RMB',
        nameTextStyle: {
          fontSize: 12
        },
        axisLabel: {
          fontSize: 11
        }
      },
      series: [
        {
          name: 'Minimum Consumption',
          type: 'bar',
          stack: 'total',
          data: consumptionData.map(item => item.min),
          itemStyle: {
            color: '#fac858'
          },
          label: {
            show: true,
            position: 'inside',
            formatter: function (params) {
              return params.value;
            },
            fontSize: 9,
            color: '#fff'
          }
        },
        {
          name: 'Additional Consumption',
          type: 'bar',
          stack: 'total',
          data: consumptionData.map(item => item.max - item.min),
          itemStyle: {
            color: '#ee6666'
          },
          label: {
            show: true,
            position: 'inside',
            formatter: function (params) {
              return params.value > 0 ? `+${params.value}` : '';
            },
            fontSize: 9,
            color: '#fff'
          }
        }
      ],
      dataZoom: [
        {
          type: 'inside',
          start: 0,
          end: 40
        },
        {
          type: 'slider',
          start: 0,
          end: 40,
          bottom: '2%',
          height: 20
        }
      ]
    };

    consumptionChartInstance.setOption(option);

    window.addEventListener('resize', () => {
      if (consumptionChartInstance) {
        consumptionChartInstance.resize();
      }
    });
  }, 100);
};

// 初始化营收水平柱状图
const initRevenueChart = () => {
  setTimeout(() => {
    if (!revenueChart.value) {
      console.error('Revenue chart DOM not found');
      return;
    }

    const dom = revenueChart.value;
    if (dom.clientWidth === 0 || dom.clientHeight === 0) {
      setTimeout(initRevenueChart, 100);
      return;
    }

    if (revenueChartInstance) {
      revenueChartInstance.dispose();
    }

    revenueChartInstance = echarts.init(dom);

    const option = {
      title: {
        text: 'Revenue Statistics of Major Tourist Attractions in Beijing (100 million yuan)',
        left: 'center',
        textStyle: {
          fontSize: 18,
          fontWeight: 'bold',
          color: '#333'
        }
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        },
        formatter: function (params) {
          let result = params[0].name + '<br/>';
          params.forEach(param => {
            const value = param.value;
            const seriesName = param.seriesName;
            const color = param.color;

            result += `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${color};"></span>`;

            const data = revenueData.find(item => item.name === param.name);
            if (data) {
              if (seriesName === 'Low Season Revenue') {
                const range = data.lowSeason;
                result += `${seriesName}: ${range[0]} - ${range[1]} hundred million yuan<br/>`;
              } else {
                const range = data.peakSeason;
                result += `${seriesName}: ${range[0]} - ${range[1]} hundred million yuan<br/>`;
              }
            }
          });
          return result;
        }
      },
      legend: {
        data: ['Low Season Revenue', 'Peak Season Revenue'],
        top: '7%',
        textStyle: {
          fontSize: 14
        }
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '10%',
        top: '15%',
        containLabel: true
      },
      xAxis: {
        type: 'value',
        name: '100 million yuan',
        nameTextStyle: {
          fontSize: 12
        },
        axisLabel: {
          fontSize: 11
        }
      },
      yAxis: {
        type: 'category',
        data: revenueData.map(item => item.name),
        axisLabel: {
          fontSize: 10,
          interval: 0
        },
        axisTick: {
          alignWithLabel: true
        }
      },
      series: [
        {
          name: 'Low Season Revenue',
          type: 'bar',
          data: revenueData.map(item => -item.lowSeason[1]), // 负值向左显示
          itemStyle: {
            color: '#5470c6'
          },
          label: {
            show: true,
            position: 'left',
            formatter: function (params) {
              const data = revenueData.find(item => item.name === params.name);
              return data ? `${data.lowSeason[0]} - ${data.lowSeason[1]}` : '';
            },
            fontSize: 9,
            color: '#333'
          }
        },
        {
          name: 'Peak Season Revenue',
          type: 'bar',
          data: revenueData.map(item => item.peakSeason[1]),
          itemStyle: {
            color: '#91cc75'
          },
          label: {
            show: true,
            position: 'right',
            formatter: function (params) {
              const data = revenueData.find(item => item.name === params.name);
              return data ? `${data.peakSeason[0]} - ${data.peakSeason[1]}` : '';
            },
            fontSize: 9,
            color: '#333'
          }
        }
      ],
      dataZoom: [
        {
          type: 'inside',
          yAxisIndex: 0,
          start: 0,
          end: 40
        },
        {
          type: 'slider',
          yAxisIndex: 0,
          start: 0,
          end: 40,
          bottom: '2%',
          height: 20
        }
      ]
    };

    revenueChartInstance.setOption(option);

    window.addEventListener('resize', () => {
      if (revenueChartInstance) {
        revenueChartInstance.resize();
      }
    });
  }, 100);
};


// 路线数据
const routeData = ref({
  route: [
    "The Palace Museum",
    "Shichahai Lakes Area",
    "Summer Palace",
    "Temple of Heaven"
  ],
  steps: [
    {
      from: "The Palace Museum",
      to: "Shichahai Lakes Area",
      public_transport_route: "Tian'anmen West Station (Line 1) → Nanpu Station (Line 1→Line 8) → Shichahai Station (Line 8)",
      distance_km: 2.0,
      time_min: 15,
      taxi_price_yuan: 13.0
    },
    {
      from: "Shichahai Lakes Area",
      to: "Summer Palace",
      public_transport_route: "Shichahai Station (Line 8) → Nanpu Station (Line 8→Line 1) → Xidan Station (Line 1→Line 4) → Summer Palace Station (Line 4)",
      distance_km: 14.3,
      time_min: 45,
      taxi_price_yuan: 60.0
    },
    {
      from: "Summer Palace",
      to: "Temple of Heaven",
      public_transport_route: "Summer Palace Station (Line 4) → Xidan Station (Line 4→Line 1) → Dongdan Station (Line 1→Line 5) → Temple of Heaven East Gate Station (Line 5)",
      distance_km: 20.0,
      time_min: 50,
      taxi_price_yuan: 55.0
    }
  ],
  total_time_min: 110.0,
  total_distance_km: 36.3,
  total_price_yuan: 128.0,
  success: true
});

// 路线图实例
const routeChart = ref(null);
let routeChartInstance = null;

// 初始化路线图
const initRouteChart = () => {
  setTimeout(() => {
    if (!routeChart.value) {
      console.error('Route chart DOM not found');
      return;
    }

    const dom = routeChart.value;
    if (routeChartInstance) {
      routeChartInstance.dispose();
    }

    routeChartInstance = echarts.init(dom);

    // 创建路线图数据
    const routePoints = routeData.value.route;
    const steps = routeData.value.steps;
    
    // 创建节点数据
    const nodes = routePoints.map((point, index) => {
      return {
        name: point,
        x: index * 100,
        y: 50,
        symbolSize: 30,
        itemStyle: {
          color: index === 0 || index === routePoints.length - 1 ? '#c33' : '#409eff'
        }
      };
    });
    
    // 创建连线数据
    const links = steps.map((step, index) => {
      return {
        source: step.from,
        target: step.to,
        lineStyle: {
          color: '#91cc75',
          width: 3,
          curveness: 0.2
        },
        label: {
          show: true,
          formatter: `${step.distance_km}km / ${step.time_min}min`,
          fontSize: 10
        }
      };
    });

    const option = {
      title: {
        text: 'Beijing Recommended Tourist Route',
        left: 'center',
        textStyle: {
          fontSize: 18,
          fontWeight: 'bold',
          color: '#333'
        }
      },
      tooltip: {
        formatter: function (params) {
          if (params.dataType === 'node') {
            return params.data.name;
          } else if (params.dataType === 'edge') {
            const step = steps[params.dataIndex];
            return `${step.from} → ${step.to}<br/>
                    距离: ${step.distance_km}公里<br/>
                    时间: ${step.time_min}分钟<br/>
                    出租车费用: ${step.taxi_price_yuan}元`;
          }
        }
      },
      animation: true,
      series: [{
        type: 'graph',
        layout: 'none',
        symbolSize: 50,
        roam: true,
        label: {
          show: true,
          position: 'bottom',
          formatter: '{b}',
          fontSize: 12
        },
        edgeSymbol: ['circle', 'arrow'],
        edgeSymbolSize: [4, 10],
        edgeLabel: {
          fontSize: 10
        },
        data: nodes,
        links: links,
        lineStyle: {
          opacity: 0.9,
          width: 2,
          curveness: 0.1
        }
      }]
    };

    routeChartInstance.setOption(option);

    window.addEventListener('resize', () => {
      if (routeChartInstance) {
        routeChartInstance.resize();
      }
    });
  }, 100);
};

// 在onMounted中添加初始化路线图
onMounted(() => {
  setTimeout(() => {
    initStackedBarChart();
    initRevenueChart();
    initConsumptionChart();
    initRouteChart(); // 添加这一行
  }, 300);
});




// 组件卸载时清理
import { onUnmounted } from 'vue';
onUnmounted(() => {
  if (chartInstance) {
    chartInstance.dispose();
    chartInstance = null;
  }
  if (revenueChartInstance) {
    revenueChartInstance.dispose();
    revenueChartInstance = null;
  }
  if (consumptionChartInstance) {
    consumptionChartInstance.dispose();
    consumptionChartInstance = null;
  }
  if (routeChartInstance) {
    routeChartInstance.dispose();
    routeChartInstance = null;
  }
});
</script>

<style scoped>
.team-knowledge {
  padding: 20px;
  background-color: #f2ece6;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0px;
  background-color: #f2ece6;
}

.document-list {
  margin-bottom: 20px;
  background-color: #f2ece6;
}

/* 图表容器样式 */
.chart-container {
  width: 100%;
  height: 500px;
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.stacked-bar-chart,
.revenue-chart,
.consumption-chart {
  width: 100%;
  height: 100%;
  min-height: 400px;
}

/* 修改 Element Plus 组件样式 */
::v-deep(.el-card) {
  border: none;
  background-color: #f2ece6 !important;
  box-shadow: none;
}

.logo-container {
  position: relative;
  display: block;
  width: 100%;
  height: 500px;
}

.logo-container img {
  width: 200px;
  height: 40px;
}

.logo-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #f2ece6;
  font-size: 70px;
  font-weight: bold;
  text-align: center;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .chart-container {
    height: 500px;
    padding: 10px;
  }

  .logo-text {
    font-size: 40px;
  }

  .summary-item {
    min-width: 100%;
  }
}


.route-info {
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
  margin-top: 20px;
}

.route-summary {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 15px;
}

.summary-item {
  background-color: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  flex: 1;
  min-width: 200px;
  text-align: center;
}

.summary-item h3 {
  font-size: 16px;
  color: #666;
  margin-bottom: 8px;
}

.summary-item p {
  font-size: 24px;
  font-weight: bold;
  color: #c33;
}

.route-steps {
  margin-top: 20px;
}

.step-item {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 15px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.step-header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.step-number {
  background-color: #c33;
  color: white;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 10px;
  font-weight: bold;
}

.step-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.step-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 15px;
  margin-top: 15px;
}

.detail-item {
  background-color: #f8f9fa;
  padding: 12px;
  border-radius: 6px;
}

.detail-item h4 {
  font-size: 14px;
  color: #666;
  margin-bottom: 5px;
}

.detail-item p {
  font-size: 16px;
  color: #333;
}

.transport-icon {
  display: inline-block;
  width: 20px;
  height: 20px;
  background-color: #409eff;
  color: white;
  border-radius: 50%;
  text-align: center;
  line-height: 20px;
  margin-right: 5px;
  font-size: 12px;
}

</style>