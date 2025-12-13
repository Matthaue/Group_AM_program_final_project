简要说明

本项目包含一个**旅游景点智能路线规划工具**，可根据用户输入的起点、终点、必去/可选/不可去景点及约束条件（时间、距离、价格），自动计算最优旅游路线。项目可用于旅行辅助决策、路线推荐、行程安排自动化等应用场景。

主要功能

pt.py taxi.py和merge_data.py用于清理与整合数据文件

data.py是数据提取模块，用于后面路径规划

route.py是主要的路径规划功能，为了方便前端网站，通过输入输出json文件来规划路径

user_input.json是用户输入路线规划的信息文件
{
    "start": "The Forbidden City",          #起点
    "end": "Temple of Heaven",          #终点
    "must_visit": ["Summer Palace", "Shichahai"],          #必经景点
    "can_visit": [],          #不超过限制下可去的景点
    "not_visit": ["Badaling Great Wall"],          #不去景点
    "max_time": 180,          #最大时间（分钟）
    "max_dist": 50.0,          #最大距离（公里）
    "max_price": 200.0,          #最大价格（元）
    "mode": "time"          #路径规划主目标，可为 "distance"（距离最短）、"time"（用时最短）、"price"（费用最省）
}

以下是按照上面这个输入数据的例子得到的结果
{
  "route": [          #路线
    "The Forbidden City",
    "Shichahai",
    "Summer Palace",
    "Temple of Heaven"
  ],
  "steps": [          #景点之间的路线、距离、时间和价格
    {
      "from": "The Forbidden City",
      "to": "Shichahai",
      "public_transport_route": "Tian'anmen West Station (Line 1) → Nanpu Station (Line 1→Line 8) → Shichahai Station (Line 8)",
      "distance_km": 2.0,
      "time_min": 15,
      "taxi_price_yuan": 13.0
    },
    {
      "from": "Shichahai",
      "to": "Summer Palace",
      "public_transport_route": "Shichahai Station (Line 8) → Nanpu Station (Line 8→Line 1) → Xidan Station (Line 1→Line 4) → Summer Palace Station (Line 4)",
      "distance_km": 14.3,
      "time_min": 45,
      "taxi_price_yuan": 60.0
    },
    {
      "from": "Summer Palace",
      "to": "Temple of Heaven",
      "public_transport_route": "Summer Palace Station (Line 4) → Xidan Station (Line 4→Line 1) → Dongdan Station (Line 1→Line 5) → Temple of Heaven East Gate Station (Line 5)",
      "distance_km": 20.0,
      "time_min": 50,
      "taxi_price_yuan": 55.0
    }
  ],          #总用时、距离、价格和是否成功规划路线
  "total_time_min": 110.0,
  "total_distance_km": 36.3,
  "total_price_yuan": 128.0,
  "success": true
}


# Front-end

## Front-end Display Module

* Technology stack: Vite + ECharts (data visualization) + Element UI (component library)

* Core functions: route result display, attraction data visualization

## Front-end Project Files


| File / Directory Path                         | 	Function Description          |
| --------------------------------------------- | -------------- |
| `src/pages/home/home.vue`                     | Front-end homepage (user demand input interface) |
| `src/pages/scenicAreaData/scenicAreaData.vue` | Attraction data display page        |
| `src/figure`                                  | Directory for storing image resources needed by the front-end webpage |
| `package-lock.json`                           | Front-end project dependency configuration file    |

## Usage Instructions

### Front-end Running Steps



1. **Dependency Installation**: Enter the root directory of the front-end project and execute the following command to install dependencies (Node.js needs to be installed in advance):


```
npm install
```



1. **Local Running**: After the dependencies are installed, execute the following command to start the local service:



```
npm run dev
```



1. **Page Access**：After successful startup, access the front-end page according to the local address prompted in the terminal (such as http://127.0.0.1:5173/)

2. **Page Switching**：Switch between the "Home" and "Beijing Scenic Area Data" through the top navigation bar