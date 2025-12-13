<template>
    <div class="team-knowledge">
        <div class="page-header">
            <div class="logo-container">
                <!-- 轮播图容器 -->
                <div class="carousel-container">
                    <el-carousel :style="{ width: '100%', height: '500px' }" indicator-position="none" arrow="always"
                        :autoplay="true" :interval="3000">
                        <el-carousel-item v-for="item in figureImages" :key="item.id">
                            <div class="carousel-item-bg" :style="{ backgroundImage: `url(${item.src})` }"></div>
                        </el-carousel-item>
                    </el-carousel>
                </div>
                <div class="logo-text">Beijing Scenic Area Route Planning</div>
            </div>
        </div>

        <!-- 文档列表 -->
        <!-- 故宫 -->
        <el-card class="document-list">
            <el-collapse v-model="gugongMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/gugong_main.jpg" alt="gugong" style="width: 100%; height: 100%;">
                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>The Palace Museum</h2>
                                <p>Located at No. 4 Jingshanqian Street, Dongcheng District, Beijing, it is the largest
                                    and best-preserved ancient wooden architectural complex existing in the world. It is
                                    also a royal palace complex of the Ming and Qing dynasties, carrying profound
                                    historical and cultural significance.
                                    Its opening hours are closed on Mondays and open from Tuesday to Sunday. The
                                    specific time is 8:30-17:00 (admission stops at 16:00). The average visiting time is
                                    3-4 hours. Peak tourist flows mainly occur during holidays, weekends, and peak
                                    travel seasons such as August and October.</p>
                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for the Palace Museum</h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>Peak season (Apr 1 - Oct 31): 60 RMB per person for the main entrance; Off-season (Nov 1 -
                            Mar 31 next year): 40
                            RMB per person. The Treasure Gallery and Clock Gallery are 10 RMB per person each.</p>
                        <h2>Preferential Policies</h2>
                        <p>For students aged 18 and above with undergraduate or below academic qualifications,
                            the student ticket for the main entrance is 20 RMB, and 5 RMB each for the Treasure Gallery
                            and Clock Gallery.
                            For seniors aged 60 and above, the main entrance ticket is half-price (30 RMB in peak
                            season, 20 RMB in
                            off-season),
                            and 5 RMB each for the Treasure Gallery and Clock Gallery. Minors under 18, people with
                            disabilities, active
                            military personnel,
                            fire rescue personnel, retired cadres, etc., are free with valid documents.
                            Those holding local social security payment certificates enjoy half-price tickets. In
                            addition,
                            women get half-price tickets on International Women's Day,
                            and relatives of military personnel and other related groups can visit for free on Army Day
                            (Aug 1).</p>
                        <!-- <p>故宫以三大殿为中心，占地面积约72万平方米，建筑面积约15万平方米...</p> -->

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="gugongChartContainer" id="gugongChartContainer" class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (56% female, 44% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Tourist Type Distribution</h4>
                                <div ref="gugongPieChartContainer" id="gugongPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Tourist type distribution (Team 55%, Individual 45%)
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age Distribution</h4>
                                <div ref="gugongAgeChartContainer" id="gugongAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (Over 40: 54%, 20-40: 31%, Under 20: 15%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>Central Axis Complex</h3>
                                <li>Entering through the Meridian Gate, the Hall of Supreme Harmony, Hall of Central
                                    Harmony,
                                    and Hall of Preserving Harmony inside the Gate of Supreme Harmony form the core of
                                    the "Outer Court".
                                    Known as the "Golden Throne Hall", the Hall of Supreme Harmony was where emperors of
                                    the Ming and Qing
                                    dynasties held grand ceremonies.
                                    Its coiled dragon gold pillars and double-eave gabled roof reflect the highest
                                    architectural rank.
                                    The Palace of Heavenly Purity, Palace of Union, and Palace of Earthly Tranquility
                                    make up the "Inner
                                    Court".
                                    The Palace of Heavenly Purity served as the imperial bedroom before Emperor Kangxi’s
                                    reign,
                                    and the secret imperial succession edict was once hidden behind the "Upright and
                                    Pure" plaque.</li>
                                <h3></h3>
                                <h3>Eastern and Western Six Palaces & Thematic Exhibitions</h3>

                                <li>The Eastern Six Palaces, including the Palace of Eternal Spring and Palace of
                                    Prolonged Blessing,
                                    record the daily life of imperial concubines. The Western Six Palaces’ Palace of
                                    Gathered Elegance was
                                    once the residence of Empress Dowager Cixi,
                                    with its interior furnishings retaining the late Qing style. The Clock and Watch
                                    Gallery, converted from
                                    the Ancestral Temple,
                                    houses over 1,500 Chinese and foreign timepieces—among them, the "Bronze Gilded
                                    Clock with Writing
                                    Figure" can automatically write Chinese characters.
                                    The Treasure Gallery displays national treasures such as the jade mountain sculpture
                                    "Yu the Great
                                    Taming the Flood".
                                    Separate tickets are required for both galleries.</li>
                                <h3> </h3>
                                <h3>Imperial Garden & Corner Towers</h3>
                                <li>Located at the northern end of the Forbidden City, the Imperial Garden is an
                                    exquisite landscape
                                    composed of ancient cypresses, rockeries, and pavilions.
                                    After exiting through the Gate of Divine Might, you can climb Jingshan Hill to
                                    overlook the panoramic
                                    view of "a sea of golden tiles".
                                    The four corner towers, combining multi-eave pointed roofs and gabled and hip roofs,
                                    are classic symbols
                                    of Chinese architecture.
                                    Their reflection in the moat at dawn is a masterpiece for photography.</li>
                                <!-- <li>回音壁</li> -->
                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 天坛 -->
        <el-card class="document-list">
            <el-collapse v-model="tiantanMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/tiantan_main.jpg" alt="tiantan"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Temple of Heaven</h2>
                                <p>Located at No. 7 Tiantan Neidongli, Dongcheng District, Beijing, it was the venue for
                                    emperors of the Ming and Qing dynasties to "worship heaven" and "pray for grain".
                                    First built in the 18th year of Yongle in the Ming Dynasty (1420), it is the largest
                                    existing ancient sacrificial architectural complex in China.
                                    Together with the Palace Museum, it has been included in the UNESCO "World Heritage
                                    List".
                                    The architecture of Tiantan represents the culmination of architectural
                                    craftsmanship in the Ming and Qing dynasties. With the Circular Mound Altar and the
                                    Hall of Prayer for Good Harvests as representatives,
                                    its layout, structure and decoration all reflect profound cultural heritage.</p>
                                <p>Opening Hours: Peak season (Apr 1 - Oct 31): 6:00-22:00 (last entry at 21:00);
                                    Off-season (Nov 1 - Mar 31): 6:30-22:00 (last entry at 21:00).
                                    The scenic courtyards open at 8:00, with last entry at 16:30 in off-season and 17:30
                                    in peak season.</p>


                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for Temple of Heaven</h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>Peak season (Apr 1 - Oct 31): 15 RMB per person for the main entrance ticket, 34 RMB per
                            person for
                            the combined ticket; Off-season (Nov 1 - Mar 31 next year): 10 RMB per person for the main
                            entrance
                            ticket, 28 RMB per person for the combined ticket.</p>
                        <h2>Preferential Policies</h2>
                        <p>Students aged 18 and above with undergraduate or below academic qualifications, and those
                            holding
                            social security payment certificates can purchase half-price tickets. Visitors aged 60 and
                            above are
                            exempt from the main entrance ticket—for scenic spots like the Hall of Prayer for Good
                            Harvests
                            included in the combined ticket, visitors aged 60-64 get half-price, and those aged 65 and
                            above are
                            free. Minors under 18, people with disabilities, active and retired military personnel, fire
                            rescue
                            personnel, etc., are free with valid documents. Taiwan compatriots holding newly issued
                            Taiwan
                            Compatriot Travel Permits can visit for free within one year.</p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="tiantanChartContainer" id="tiantanChartContainer" class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (55% female, 45% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Tourist Type Distribution</h4>
                                <div ref="tiantanPieChartContainer" id="tiantanPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Tourist type distribution (Team 40%, Individual 60%)
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age Distribution</h4>
                                <div ref="tiantanAgeChartContainer" id="tiantanAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 50%, 20-40: 40%, under 20: 10%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Hall of Prayer for Good Harvests
                                </h3>
                                <li>
                                    The iconic building of the Temple of Heaven, it features a triple-eave circular
                                    pointed roof
                                    covered with dark blue glazed tiles symbolizing the celestial dome. Its gilded
                                    golden top
                                    reaches 38 meters high. The internal structure hides profound meanings: the 4
                                    central
                                    "Longjing Pillars" represent the four seasons, the 12 golden pillars in the inner
                                    circle
                                    correspond to the 12 months, and the 12 eave pillars in the outer circle symbolize
                                    the 12
                                    two-hour periods of a day. The total 28 pillars echo the 28 constellations. The
                                    "Dragon and
                                    Phoenix Stone" at the center of the floor has natural grains forming dragon and
                                    phoenix
                                    patterns, which set off against the dragon and phoenix caisson ceiling above—an
                                    exquisite
                                    integration of architecture and culture.
                                </li>
                                <h3></h3>
                                <h3>
                                    Circular Mound Altar
                                </h3>
                                <li>
                                    The core venue for heaven-worshipping ceremonies, its three-layer white marble
                                    platform is
                                    arranged with "yang numbers" (odd numbers). Each circle of fan-shaped stones is a
                                    multiple
                                    of 9, extending from the center to 81 stones (9×9). The "Heavenly Heart Stone" at
                                    the
                                    altar’s center is an acoustic miracle—standing on it, one’s voice produces a strong
                                    echo as
                                    if communicating with heaven. Twenty-two emperors of the Ming and Qing dynasties
                                    held 654
                                    sacrificial rituals here.
                                </li>
                                <h3></h3>
                                <h3>
                                    Imperial Vault of Heaven & Echo Wall
                                </h3>
                                <li>
                                    The Imperial Vault of Heaven is an auxiliary building of the Circular Mound Altar,
                                    used to
                                    enshrine the memorial tablet of the Supreme Heavenly Emperor. Its circular
                                    surrounding wall
                                    is the famous "Echo Wall". Two people standing at the east and west walls
                                    respectively can
                                    converse clearly, demonstrating the ancient wisdom in acoustic application.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 颐和园 -->
        <el-card class="document-list">
            <el-collapse v-model="yiheyuanMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/yiheyuan_main.jpg" alt="yiheyuan"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>
                                    Summer Palace
                                </h2>
                                <p>
                                    Located at No. 19 Xinjian Gongmen Road, Haidian District, Beijing, it is China’s
                                    largest and best-preserved imperial garden, and one of the world’s famous scenic
                                    spots. With a history of over 800 years, it covers an area of 290 hectares, of which
                                    Kunming Lake accounts for two-thirds.
                                    Centered on the Tower of Buddhist Incense, the garden features various architectures
                                    including towers, terraces, pavilions, corridors, halls and boats. Each structure
                                    has its own characteristics while integrating harmoniously. Scenic spots like the
                                    Garden of Harmonious Interests and Suzhou Street boast unique charms.
                                </p>
                                <p>
                                    Opening Hours: Peak season (Apr 1 - Oct 31): Opens at 6:00, last entry at 19:00,
                                    closes at 20:00; Off-season (Nov 1 - Mar 31): Opens at 6:30, last entry at 18:00,
                                    closes at 19:00.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>
                            Basic Ticket Prices
                        </h2>
                        <p>
                            Peak season (Apr 1 - Oct 31): 30 RMB per person for the main entrance ticket, 60 RMB per
                            person for
                            the combined ticket; Off-season (Nov 1 - Mar 31 next year): 20 RMB per person for the main
                            entrance
                            ticket, 50 RMB per person for the combined ticket.
                        </p>
                        <h2>
                            Preferential Policies
                        </h2>
                        <p>Visitors aged 60 and above can enter for free with valid documents such as ID cards. Special
                            groups
                            including minors under 18, people with disabilities, and active military personnel are free
                            with
                            valid documents. Students aged 18 and above with undergraduate or below academic
                            qualifications, and
                            those holding social security payment certificates are eligible for half-price tickets.
                        </p>


                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="yiheyuanChartContainer" id="yiheyuanChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (54% female, 46% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="yiheyuanPieChartContainer" id="yiheyuanPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 35% , individual 65% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="yiheyuanAgeChartContainer" id="yiheyuanAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 45%, 20-40: 40%, under 20: 15%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    East Palace Gate Area
                                </h3>
                                <li>
                                    Entering through the main East Palace Gate, you’ll find the Hall of Benevolence and
                                    Longevity—where Empress Dowager Cixi and Emperor Guangxu handled state affairs. The
                                    dragon
                                    throne and screen inside retain their original late Qing appearance. To the south,
                                    the Grand
                                    Theater in the Garden of Virtue and Harmony is the largest opera house of the Qing
                                    Dynasty.
                                    Its three-story stage features secret passages and lifting devices to stage scenes
                                    of gods,
                                    immortals, ghosts and monsters, and Empress Dowager Cixi once watched plays here for
                                    dozens
                                    of days.
                                </li>
                                <h3></h3>
                                <h3>
                                    Long Corridor & Longevity Hill
                                </h3>
                                <li>
                                    Stretching 728 meters from the Moon-inviting Gate in the east to the Stone Tablet
                                    Pavilion
                                    in the west, the Long Corridor is adorned with over 14,000 paintings on its beams.
                                    Covering
                                    landscapes, figures and historical allusions, it is hailed as the "longest painted
                                    corridor
                                    in the world". At the end of the corridor, the Hall of Dispelling Clouds is built
                                    against
                                    the mountain. Climbing the steps leads to the Tower of Buddhist Incense, the highest
                                    point
                                    of the garden at 41 meters. Ascending the tower offers a panoramic view of Kunming
                                    Lake,
                                    with the best perspective of the lake from the middle section of the steps.
                                </li>
                                <h3></h3>
                                <h3>
                                    Kunming Lake & West Causeway
                                </h3>
                                <li>
                                    Modeled after Su Causeway of West Lake, the West Causeway crosses the lake, with six
                                    bridges
                                    spanning it. Among them, the Jade Belt Bridge is built of white marble, boasting a
                                    graceful
                                    curve like a jade belt. The 17-Arch Bridge at the southeast end connects the east
                                    bank to
                                    South Lake Island, with its archways arranged symmetrically. At sunset in winter,
                                    sunlight
                                    penetrates the archways, creating the spectacular "Golden Light Through Arches"
                                    scene. The
                                    Marble Boat (Clear and Peaceful Boat) by the lake is a Sino-Western hybrid building,
                                    where
                                    Empress Dowager Cixi often rested and enjoyed the scenery.
                                </li>
                                <h3></h3>
                                <h3>
                                    Garden of Harmonious Interests & Suzhou Street
                                </h3>
                                <li>
                                    Located in the northeast corner, the Garden of Harmonious Interests is modeled after
                                    Jichang
                                    Garden in Wuxi. Centered around a small lake and surrounded by pavilions and
                                    waterside
                                    pavilions, it is known as the "Garden within a Garden". Inside the North Palace
                                    Gate, Suzhou
                                    Street is built to imitate the water towns of Jiangnan, with lined shops restoring
                                    the style
                                    of imperial markets in the Qing Dynasty.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 圆明园 -->
        <el-card class="document-list">
            <el-collapse v-model="yuanmingyuanMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/yuanmingyuan_main.jpg" alt="yuanmingyuan"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Old Summer Palace Ruins Park</h2>
                                <p>
                                    Located at No. 28 Qinghua West Road, Haidian District, Beijing, it was a famous
                                    large-scale imperial garden of the Qing Dynasty. Composed of Yuanmingyuan, Changchun
                                    Garden and Qichun Garden, it is also known as the "Three Gardens of Yuanming" and
                                    once hailed as the "Garden of Gardens".
                                    The park featured beautiful scenery and diverse architectural styles, including
                                    traditional Chinese garden buildings and Western-style structures. However, in 1860,
                                    the British and French allied forces looted and burned the garden, reducing it to
                                    ruins. Today’s remaining walls and debris are a witness to modern Chinese history.
                                </p>
                                <p>
                                    Opening Hours: Apr 1 - Oct 31: Park gates open at 6:00, ticket sales and admission
                                    stop at 19:00, closes at 21:00; Nov 1 - Mar 31 next year: Opens at 6:30, ticket
                                    sales and admission stop at 17:30, closes at 19:30.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            10 RMB per person for the main entrance ticket, 15 RMB per person for the Western-style
                            Building
                            Ruins Scenic Area, 10 RMB per person for the Panoramic Model Exhibition, and 25 RMB per
                            person for
                            the all-inclusive ticket.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Students aged 18 and above with undergraduate or below academic qualifications, and those
                            holding
                            social security payment certificates can purchase half-price tickets (10 RMB for the
                            all-inclusive
                            ticket). Minors under 18, seniors aged 60 and above, people with disabilities, active and
                            retired
                            military personnel, fire rescue personnel, etc., are free with valid documents. Model
                            workers at or
                            above the provincial and ministerial level and righteous and courageous individuals can also
                            enter
                            for free with relevant certificates. The entire park is free of charge on Cultural Heritage
                            Day,
                            National Defense Day, and October 18th (the anniversary of the garden’s destruction) every
                            year.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="yuanmingyuanChartContainer" id="yuanmingyuanChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (52% female, 48% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="yuanmingyuanPieChartContainer" id="yuanmingyuanPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 30% , individual 70% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="yuanmingyuanAgeChartContainer" id="yuanmingyuanAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 55%, 20-40: 35%, under 20: 10%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Western-Style Building Ruins Area
                                </h3>
                                <li>
                                    As China’s earliest Western-style architectural complex, it was designed by the
                                    Italian
                                    Jesuit missionary Giuseppe Castiglione, including scenic spots such as Harmony of
                                    Interests,
                                    Garden of Peaceful Seas, and Grand Waterworks. The twelve bronze animal heads (with
                                    human
                                    bodies) in front of the Garden of Peaceful Seas once served as the core of the
                                    fountain, and
                                    the surviving heads are scattered around the world. The fragmented stone pillars of
                                    the
                                    Grand Waterworks Ruins are a iconic symbol of the Old Summer Palace, demonstrating
                                    the grand
                                    scale of Western-style architecture in those days.
                                </li>
                                <h3></h3>
                                <h3>
                                    Panoramic Model Exhibition
                                </h3>
                                <li>
                                    Located in the exhibition hall, it restores the full view of the Old Summer Palace
                                    at its
                                    peak in a 1:150 scale. Through the model, you can intuitively feel the layout of "a
                                    garden
                                    within a garden" and the architectural style, which is more immersive with light and
                                    shadow
                                    introductions.
                                </li>
                                <h3></h3>
                                <h3>
                                    Qichun Garden & Changchun Garden
                                </h3>
                                <li>
                                    Qichun Garden is dominated by traditional Chinese gardens, and the existing Zhengjue
                                    Temple
                                    is the only building in the garden that escaped destruction by fire. The Lion Grove
                                    in the
                                    northeast corner of Changchun Garden was modeled after Suzhou’s Lion Grove, and the
                                    ruins of
                                    rockeries and waterside pavilions still retain their charm.
                                </li>
                                <h3>
                                    Lotus Scenery
                                </h3>
                                <li>
                                    In summer, nearly 1,000 mu of lotus flowers bloom in the garden. Walking along the
                                    lakeside
                                    path, you can enjoy the scenery of "endless green lotus leaves reaching the sky".
                                    Cultural
                                    activities are often held during the Lotus Festival.
                                </li>
                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 八达岭长城 -->
        <el-card class="document-list">
            <el-collapse v-model="changchengMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/changcheng_main.jpg" alt="changcheng"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>
                                    Badaling Great Wall
                                </h2>
                                <p>
                                    Located at the northern entrance of Guangu Gou Ancient Road, Jundu Mountain, Yanqing
                                    District, Beijing, it is over 70 kilometers away from downtown. As the
                                    best-preserved and most representative section of the Ming Great Wall, it was
                                    historically known as one of the "Nine Fortresses Under Heaven" and a forward
                                    outpost of Juyongguan Pass—an important gateway of the Great Wall. Standing at an
                                    altitude of 1,015 meters, it boasts a strategic location and solid city gates,
                                    having always been a contested military stronghold.
                                    The pass city of Badaling Great Wall is a trapezoid narrowing eastward and widening
                                    westward, with two gates: the east gate inscribed with "Juyong Outer Town" and the
                                    west gate with "Northern Lock and Key". Currently, 3,741 meters of the wall is open
                                    to the public, including 21 crenellated watchtowers and wall platforms.
                                </p>
                                <p>
                                    Opening Hours: Generally 6:30-16:30, subject to seasonal adjustments.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            Peak season (Apr 1 - Oct 31): 40 RMB per adult; Off-season (Nov 1 - Mar 31 next year): 35
                            RMB per
                            adult. Cable car and other transportation fees are not included.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            For students aged 18 and above with undergraduate or below academic qualifications, and
                            those
                            holding social security payment certificates, the discounted ticket is 20 RMB in peak season
                            and
                            17.5 RMB in off-season. Minors under 18, seniors aged 60 and above, people with
                            disabilities, active
                            military personnel and their families (limited to 1 person), disabled military personnel,
                            military
                            dependents, retired military cadres, fire rescue personnel, etc., are free with valid
                            documents.
                            Foreign citizens shall follow the corresponding policies.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="changchengChartContainer" id="changchengChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (50% female, 50% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="changchengPieChartContainer" id="changchengPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 60% , individual 40% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="changchengAgeChartContainer" id="changchengAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 30%, 20-40: 50%, under 20: 20%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Pass City & Watchtowers
                                </h3>
                                <li>
                                    The city tower of the west gate "Northern Lock and Key" is the core of the pass
                                    city, with
                                    ancient weapons and garrison equipment displayed inside. The watchtowers along the
                                    route
                                    vary in shape—among them, the 8th North Watchtower at the top of "Hero Slope" is the
                                    highest-elevation watchtower. Climbing it offers a distant view of rolling
                                    mountains, with
                                    the Great Wall winding like a giant dragon along the mountain ridges.
                                </li>
                                <h3></h3>
                                <h3>
                                    Great Wall Museum
                                </h3>
                                <li>
                                    Located at the scenic area entrance, it showcases the Great Wall’s historical
                                    evolution,
                                    architectural craftsmanship and military culture through cultural relics, models and
                                    multimedia. The Ming Dynasty garrison artillery and city brick specimens are
                                    particularly
                                    representative.
                                </li>
                                <h3></h3>
                                <h3>
                                    Scenery Across Seasons
                                </h3>
                                <li>
                                    Spring brings blooming flowers covering the slopes, summer features layers of green
                                    trees
                                    like clouds, autumn adorns the mountains with deep red foliage, and winter presents
                                    vast
                                    snow-covered ridges. Zhao Puchu once praised its four-season scenery with the line
                                    "Through
                                    spring, autumn, winter and summer, its grandeur remains unchanged".
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 北海公园 -->
        <el-card class="document-list">
            <el-collapse v-model="beihaiMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/beihai_main.jpg" alt="beihai" style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>
                                    Beihai Park
                                </h2>
                                <p>
                                    Located at No. 1 Wenjin Street, Xicheng District, Beijing, it is the earliest-built,
                                    best-preserved and most culturally profound classical imperial garden existing in
                                    China. First constructed in the 6th year of Dading in the Jin Dynasty (1166 AD), the
                                    park has a history of over 850 years. As a masterpiece of the "one lake with three
                                    mountains" garden layout, it covers an area of 68.2 hectares, including 38.9
                                    hectares of water and 29.3 hectares of land.
                                    Qionghua Island is a key scenic area in the park. Decorated with Taihu stones moved
                                    from Genyue Garden, a famous garden of the Northern Song Dynasty, the island boasts
                                    pleasant scenery. "Autumn Wind over Taiye Lake" and "Spring Shade on Qionghua
                                    Island" were listed as two of the "Eight Scenes of Yanjing" as early as the
                                    Mingchang period of the Jin Dynasty. The White Pagoda on the island is the iconic
                                    building of the park.
                                </p>
                                <p>
                                    Opening Hours: Peak season (Apr 1 - Oct 31): 6:00-21:00 (last entry at 20:30);
                                    Off-season (Nov 1 - Mar 31): 6:30-20:00 (last entry at 19:30).
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            Peak season (Apr 1 - Oct 31): 10 RMB per person for the main entrance ticket, 20 RMB per
                            person for
                            the combined ticket; Off-season (Nov 1 - Mar 31 next year): 5 RMB per person for the main
                            entrance
                            ticket, 15 RMB per person for the combined ticket.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Seniors aged 60 and above are exempt from the main entrance ticket with valid documents.
                            Special
                            groups including minors under 18, people with disabilities, and active military personnel
                            can enter
                            for free. Students aged 18 and above with undergraduate or below academic qualifications,
                            and those
                            holding social security payment certificates are eligible for half-price tickets. Taiwan
                            compatriots
                            holding newly issued Taiwan Compatriot Travel Permits can visit for free within one year.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="beihaiChartContainer" id="beihaiChartContainer" class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (55% female, 45% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="beihaiPieChartContainer" id="beihaiPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 45% , individual 55% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="beihaiAgeChartContainer" id="beihaiAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 40%, 20-40: 40%, under 20: 20%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Qionghua Island & White Pagoda
                                </h3>
                                <li>
                                    Standing 32 meters high, the island is crowned by the White Pagoda—built in the 8th
                                    year of
                                    Shunzhi in the Qing Dynasty (1651). The 35.9-meter-tall pagoda, with a brick and
                                    stone
                                    structure capped by a gilded copper top, is the iconic landmark of Beihai Park.
                                    Climbing the
                                    stone steps around the island passes Yongan Temple and Zhengjue Hall, where Buddha
                                    statues
                                    and plaques are enshrined. The "Spring Shade on Qionghua Island" stele on the
                                    southeast side
                                    of the island, inscribed by Emperor Qianlong, is a prime spot for spring viewing.
                                </li>
                                <h3></h3>
                                <h3>
                                    Taiye Lake & Boating
                                </h3>
                                <li>
                                    The lake is divided into southern and northern parts: the southern part is called
                                    "Zhonghai"
                                    (connected to Zhongnanhai), and the northern part is the main body of Beihai Lake.
                                    Boat
                                    docks are available along the lakeside, offering rowboats and electric boats for
                                    rent.
                                    Boating in summer allows you to enjoy the lotus breeze and willow shadows, while an
                                    ice rink
                                    opens during the winter freezing period.
                                </li>
                                <h3></h3>
                                <h3>
                                    Round City & Nine-Dragon Wall
                                </h3>
                                <li>
                                    Located west of the park’s south gate, the Round City is a circular platform. The
                                    Chengguang
                                    Hall on the platform enshrines a jade Buddha, and the "Dushan Giant Jade Sea" in
                                    front of
                                    the hall is a precious jade carving from the Yuan Dynasty. The Nine-Dragon Wall on
                                    the north
                                    bank, built during Emperor Qianlong’s reign in the Qing Dynasty, stretches 25.86
                                    meters
                                    long. Its surface is inlaid with nine vivid dragons made of glazed bricks in yellow,
                                    green,
                                    blue and other colors, ranking among China’s three major Nine-Dragon Walls.
                                </li>
                                <h3></h3>
                                <h3>
                                    Jingshinzhai (Quiet Heart Studio) & Five-Dragon Pavilions
                                </h3>
                                <li>
                                    Jingshinzhai, located on the north bank, is modeled after Jiangnan gardens. Composed
                                    of
                                    rockeries, pools and winding corridors, this exquisite courtyard is hailed as "the
                                    best
                                    garden in Beihai". The Five-Dragon Pavilions, built by the lakeside, are connected
                                    as one,
                                    resembling a wandering dragon—once a royal venue for fishing and moon-gazing.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 雍和宫 -->
        <el-card class="document-list">
            <el-collapse v-model="yonghegongMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/yonghegong_main.jpg" alt="yonghegong"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Yonghe Temple (Lama Temple)</h2>
                                <p>As the largest and best-preserved Gelugpa sect Tibetan Buddhist temple in downtown
                                    Beijing, it is located on Yonghe Temple Street, Dongcheng District. First built in
                                    the 33rd year of Kangxi in the Qing Dynasty (1694), it was initially the Prince Yong
                                    Mansion—residence of Emperor Yongzheng before his ascension to the throne. In the
                                    9th year of Qianlong (1744), it was converted into a royal temple, boasting an
                                    extremely high architectural standard that integrates the architectural art
                                    characteristics of Han, Manchu, Mongolian, Tibetan and other ethnic groups. The
                                    temple features magnificent halls, towering ancient trees and flourishing incense.
                                    It is an excellent place to learn about Tibetan Buddhist culture and experience the
                                    solemn atmosphere of a royal temple.</p>
                                <p>Opening Hours: Apr 1 - Oct 31: 9:00-17:00 (last entry at 16:30); Nov 1 - Mar 31 next
                                    year: 9:00-16:30 (last entry at 16:00). Opening hours may be slightly adjusted on
                                    legal holidays and special religious festivals. It is recommended to check official
                                    information before visiting. The average visiting time is 1.5-2.5 hours. Peak
                                    tourist flows occur on religious festivals such as the first and fifteenth days of
                                    the lunar month, legal holidays including Spring Festival, May Day and National Day,
                                    and the 10:00-14:00 period daily.</p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>25 RMB per person; off-season ticket (Nov 1 - Mar 31 next year): 15 RMB per person.</p>
                        <h2>Preferential Policies</h2>
                        <p>Free admission for children under 1.2 meters and under 6 years old; half-price for minors
                            aged 6
                            (inclusive) to 18 (exclusive), and full-time students with undergraduate or below academic
                            qualifications (with valid documents); free admission for retired cadres, active military
                            personnel,
                            disabled military personnel and people with disabilities (with valid ID); half-price for
                            seniors
                            aged 60 (inclusive) and above (with valid documents).</p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="yonghegongChartContainer" id="yonghegongChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (65% female, 35% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="yonghegongPieChartContainer" id="yonghegongPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 30% , individual 70% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="yonghegongAgeChartContainer" id="yonghegongAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 24%, 20-40: 70.25%, under 20: 5.75%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Heavenly Kings Hall
                                </h3>
                                <li>
                                    The hall houses statues of Maitreya Buddha and the Four Heavenly Kings.
                                </li>
                                <h3></h3>
                                <h3>
                                    Main Hall of Yonghe Temple
                                </h3>
                                <li>
                                    Bronze statues of the Three Buddhas of the Three Ages and the Eighteen Arhats are
                                    enshrined
                                    inside the hall.
                                </li>
                                <h3></h3>
                                <h3>
                                    Yongyou Hall (Hall of Eternal Blessings)
                                </h3>
                                <li>
                                    Three Buddha statues carved from sandalwood are placed within the hall.
                                </li>
                                <h3></h3>
                                <h3>
                                    Dharma Wheel Hall
                                </h3>
                                <li>
                                    A masterpiece of the integration of Han and Tibetan cultures, the hall contains a
                                    bronze
                                    statue of Master Tsongkhapa. Behind the statue stands the Mountain of Five Hundred
                                    Arhats,
                                    and there is also a "Bathing Basin" made of golden nanmu.
                                </li>
                                <h3></h3>
                                <h3>
                                    Pavilion of Ten Thousand Blessings (Wanfu Pavilion)
                                </h3>
                                <li>
                                    It houses an 18-meter-high Maitreya Buddha statue carved from white sandalwood. In
                                    addition,
                                    the golden nanmu Buddha niche in Zhaofo Building (Buddha Shining Building), the east
                                    auxiliary hall in front of the pavilion, is also a stunning masterpiece.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 国博 折叠面板 -->
        <el-card class="document-list">
            <el-collapse v-model="guoboMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/guobo_main.jpg" alt="guobo" style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>National Museum of China</h2>
                                <p>
                                    Located east of Tiananmen Square, opposite the Great Hall of the People, it is one
                                    of the world’s largest museums in terms of single-building floor area and China’s
                                    richest in cultural relic collections. Housing over 1.4 million cultural relics, it
                                    covers all historical stages from ancient times to the present, comprehensively and
                                    systematically showcasing China’s long history and culture, splendid ancient
                                    civilization and magnificent revolutionary course. It is an important venue to
                                    experience the profoundness and breadth of Chinese civilization.
                                </p>
                                <p>
                                    Opening Hours: Tuesday to Sunday 9:00-17:00 (last entry at 16:00, crowd clearance
                                    starts at 16:30); closed on Mondays (except legal holidays). Opening hours may be
                                    extended during summer vacation and holidays—please confirm in advance through
                                    official channels.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            Admission is free but requires real-name reservation in advance via the official website or
                            the
                            "National Museum of China" WeChat official account, with time-slotted entry. Special
                            exhibitions may
                            charge separate fees.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Preferential policies for paid exhibitions usually include free admission for children under
                            6 years
                            old, retired cadres, active military personnel and people with disabilities (with valid
                            documents);
                            half-price for minors aged 6-18, full-time students with undergraduate or below academic
                            qualifications, and seniors over 60 years old (with valid documents). Specific details are
                            subject
                            to on-site announcements of the exhibitions.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="guoboChartContainer" id="guoboChartContainer" class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (55% female, 45% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="guoboPieChartContainer" id="guoboPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 50% , individual 50% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="guoboAgeChartContainer" id="guoboAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 38%, 20-40: 42%, under 20: 20%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    "Ancient China" Exhibition
                                </h3>
                                <li>
                                    Features precious cultural relics such as the Painted Pottery Basin with Human-Fish
                                    Pattern
                                    and the Square Zun with Four Sheep.
                                </li>
                                <h3></h3>
                                <h3>
                                    "Road to Rejuvenation" Exhibition
                                </h3>
                                <li>
                                    hows the Chinese nation’s rejuvenation journey from the Opium War to modern times.
                                </li>
                                <h3></h3>
                                <h3>
                                    Exhibition of Ancient Chinese Coins
                                </h3>
                                <li>
                                    Displays over 1,800 selected coins, presenting the development system of ancient
                                    Chinese
                                    currency.
                                </li>
                                <h3></h3>
                                <h3>
                                    Exhibition of Ancient Chinese Buddhist Sculptures
                                </h3>
                                <li>
                                    Presents the shapes and connotations of Buddhist sculptures from different regions
                                    through
                                    265 collections
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 鸟巢 -->
        <el-card class="document-list">
            <el-collapse v-model="niaochaoMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/niaochao_main.jpg" alt="niaochao"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Bird's Nest (National Stadium)</h2>
                                <p>Located in the central area of Olympic Park, Chaoyang District, it was the main
                                    stadium of the 2008 Beijing Olympic Games. Named for its unique steel structure
                                    resembling a bird's nest, it was co-designed by the Swiss architectural firm Herzog
                                    & de Meuron, China Architecture Design & Research Group, etc. With a construction
                                    area of 258,000 square meters, it was once the world’s largest steel-structured
                                    stadium and has now become one of the iconic buildings of Beijing and even China.
                                    After the Olympic Games, it continues to host international and domestic sports
                                    events, large-scale concerts, exhibitions and other activities, while opening to
                                    tourists. Visitors can tour areas such as the inner stadium, stands and Olympic
                                    exhibition hall, experiencing the integration of Olympic passion and architectural
                                    art.</p>
                                <p>Opening Hours: On non-event days, it is usually 9:00-19:00 (last entry at 18:30). If
                                    there are competitions or performances, the opening hours will be adjusted according
                                    to the event arrangement, and some areas may be temporarily closed. It is
                                    recommended to check the official announcement in advance. </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">

                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            50 RMB per person (including the visit to the internal main stadium); combined ticket for
                            "Bird's
                            Nest + Olympic Culture Exhibition": 80 RMB per person. Some experience projects such as
                            track
                            walking and sky corridor require separate payment, with prices ranging from 50 to 200 RMB.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Free admission for children under 1.2 meters (accompanied by adults); half-price for
                            children
                            1.2-1.4 meters tall, full-time students with undergraduate or below academic qualifications
                            (with
                            student ID), seniors over 60 years old (with ID card) and people with disabilities (with
                            disability
                            certificate); free admission for active military personnel with valid documents.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="niaochaoChartContainer" id="niaochaoChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (45% female, 55% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="niaochaoPieChartContainer" id="niaochaoPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 20% , individual 80% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="niaochaoAgeChartContainer" id="niaochaoAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 17%, 20-40: 58%, under 20: 25%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>

                                </h3>
                                <li>
                                    The core attraction is its unique architectural appearance—woven from a massive
                                    steel
                                    structure, it resembles a bird's nest with strong modernity and artistic appeal.
                                </li>
                                <h3></h3>
                                <h3>

                                </h3>
                                <li>
                                    The internal large-scale track and field stadium and football field can accommodate
                                    91,000
                                    people. The spectator stands surround the venue in a bowl shape, and the membrane
                                    structure
                                    roof above can both shade the sun and keep out rain.
                                </li>
                                <h3></h3>
                                <h3>

                                </h3>
                                <li>
                                    In addition, the venue is equipped with an Olympic Culture Corridor, which displays
                                    the
                                    Olympic history and related cultural relics.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 水立方 -->
        <el-card class="document-list">
            <el-collapse v-model="shuilifangMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/shuilifang_main.jpg" alt="shuilifang"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Water Cube (National Aquatics Center)</h2>
                                <p>
                                    It stands side by side with the Bird's Nest in Olympic Park and is another iconic
                                    venue of the 2008 Beijing Olympic Games. Inspired by the microcosmic structure of
                                    water bubbles, its exterior wall adopts a unique ETFE membrane material—lightweight
                                    and highly translucent. At night, under the reflection of lights, it presents a
                                    dreamy blue glow, hence the name "Water Cube". It once hosted Olympic events such as
                                    swimming, diving and synchronized swimming, setting multiple world records. After
                                    the Olympics, it underwent functional renovation, with part of the area transformed
                                    into the "Water Cube Water Park", becoming a multi-functional aquatic center
                                    integrating swimming, fitness, entertainment and event hosting.
                                </p>
                                <p>
                                    Opening Hours: Venue visit: usually 9:00-21:00; Water Park: generally 10:00-22:00
                                    (may be adjusted on holidays). If there are events, the open areas and hours will
                                    change temporarily—please confirm in advance. </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            Venue visit ticket: 30 RMB per person; Water Park ticket: 200 RMB per person on weekdays,
                            230 RMB
                            per person on weekends and holidays (discounted combination tickets are recommended to be
                            purchased
                            through official channels). Swimming cards and fitness programs need to be handled
                            separately.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Free admission for children under 1.2 meters for venue visits; children under 1.2 meters
                            need to buy
                            children's tickets for the Water Park (160 RMB on weekdays, 180 RMB on weekends and
                            holidays).
                            Children 1.2-1.5 meters tall, full-time students, seniors over 60 years old and people with
                            disabilities (with valid documents) are eligible for half-price tickets for both venue
                            visits and
                            the Water Park. Active military personnel (with valid documents) enjoy free venue visits and
                            half-price Water Park tickets.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="shuilifangChartContainer" id="shuilifangChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (52% female, 48% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="shuilifangPieChartContainer" id="shuilifangPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 25% , individual 75% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="shuilifangAgeChartContainer" id="shuilifangAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 15%, 20-40: 35%, under 20: 40%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>

                                </h3>
                                <li>
                                    The core attraction is its unique exterior facade, adopting an ETFE membrane
                                    structure that
                                    resembles a "water bubble" and presents a colorful effect under sunlight.
                                </li>
                                <h3></h3>
                                <h3>

                                </h3>
                                <li>
                                    Inside, there are large-scale swimming and diving venues. Among them, the "Water
                                    Cube Water
                                    Park" is one of Asia’s largest indoor water parks, featuring a variety of water
                                    entertainment facilities.
                                </li>
                                <h3></h3>
                                <h3>

                                </h3>
                                <li>
                                    In addition, various art exhibitions and cultural activities are held in the venue
                                    regularly.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 香山公园 -->
        <el-card class="document-list">
            <el-collapse v-model="xiangshanMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/xiangshan_main.jpg" alt="xiangshan"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Fragrant Hills Park (Xiangshan Park)</h2>
                                <p>
                                    Located in Haidian District on the western outskirts of Beijing, covering an area of
                                    188 hectares, it is a classical garden combining mountain forest features with
                                    imperial garden charm. First built in the 26th year of Dading in the Jin Dynasty
                                    (1186), it was once an imperial garden in history. During the Qianlong reign of the
                                    Qing Dynasty, Emperor Qianlong expanded it into "Jingyi Garden", making it one of
                                    the "Three Hills and Five Gardens". Famous worldwide for its red leaves covering the
                                    mountains in autumn, the best viewing period is from late October to mid-November
                                    every year. It also boasts rich historical and cultural heritage and humanistic
                                    landscapes. Climbing to the top of Incense Burner Peak (commonly known as
                                    "Guijianchou", meaning "even ghosts would fear climbing it") offers a panoramic view
                                    of Beijing, making it a premium destination for autumn appreciation, leisure and
                                    fitness, and experiencing historical heritage.
                                </p>
                                <p>
                                    Opening Hours: Apr 1 - Oct 31: 6:00-18:30 (last entry at 18:00); Nov 1 - Mar 31 next
                                    year: 6:30-18:00 (last entry at 17:30). Opening hours may be extended during the Red
                                    Leaf Festival.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            Peak season (Apr 1 - Oct 31): 10 RMB per person for the park ticket, 10 RMB per person for
                            the Biyun
                            Temple ticket; Off-season (Nov 1 - Mar 31 next year): 5 RMB per person for the park ticket,
                            10 RMB
                            per person for the Biyun Temple ticket. Cable car tickets are sold separately: 80 RMB per
                            person for
                            one-way up, 60 RMB per person for one-way down, and 120 RMB per person for a round trip.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Free admission for children under 1.2 meters, children under 6 years old, retired cadres,
                            active
                            military personnel, disabled military personnel, and people with disabilities (with valid
                            documents); half-price tickets for minors aged 6 (inclusive) to 18 (exclusive), full-time
                            students
                            with undergraduate or below academic qualifications (with student ID), and seniors aged 60
                            (inclusive) and above (with ID card); seniors holding the "Beijing Tong - Pension and
                            Disability
                            Card" can enter for free.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="xiangshanChartContainer" id="xiangshanChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (65% female, 35% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="xiangshanPieChartContainer" id="xiangshanPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 30% , individual 70% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="xiangshanAgeChartContainer" id="xiangshanAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 24%, 20-40: 70.25%, under 20: 5.75%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Incense Burner Peak (Xianglu Peak)
                                </h3>
                                <li>
                                    As the main peak of Fragrant Hills Park, it stands at an altitude of 575 meters. Its
                                    name
                                    comes from two huge milk-like rocks at the top that resemble an incense burner.
                                    Climbing to
                                    the peak (or taking the cable car for convenience) offers a panoramic view of
                                    Beijing’s
                                    urban scenery, with steep and spectacular mountain views along the way.
                                </li>
                                <h3></h3>
                                <h3>
                                    Biyun Temple (Azure Cloud Temple)
                                </h3>
                                <li>
                                    Integrating architectural styles of the Ming and Qing dynasties, the temple covers
                                    an area
                                    of about 40,000 square meters. Its main buildings stretch along the east-west axis,
                                    consisting of six courtyards in sequence, showcasing the solemnity and grandeur of
                                    traditional Chinese temple architecture.
                                </li>
                                <h3></h3>
                                <h3>
                                    Shuangqing Villa
                                </h3>
                                <li>
                                    Originally built on the site of a royal garden in the Qing Dynasty, it was later
                                    converted
                                    into a villa. In 1949, it became the first station of the Communist Party of China’s
                                    "entry
                                    to Beijing for the exam" and the temporary command center of the Central Committee.
                                    Mao
                                    Zedong lived and worked here, directing the Crossing the Yangtze River Campaign and
                                    other
                                    important events, witnessing a crucial period of China’s revolutionary history.
                                </li>
                                <h3></h3>
                                <h3>
                                    Fragrant Hills Red Leaves
                                </h3>
                                <li>
                                    With 140,000 red-leaf trees such as smoke trees, it is the park’s most renowned
                                    autumn
                                    attraction. From late October to mid-November, the mountains are covered with fiery
                                    red
                                    leaves, forming a magnificent and breathtaking scene. There are multiple viewing
                                    routes,
                                    including the imperial path and cable car route, to enjoy the scenery in different
                                    ways.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 南锣鼓巷 -->
        <el-card class="document-list">
            <el-collapse v-model="nanluoguxiangMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/nanluoguxiang_main.jpg" alt="nanluoguxiang"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Nanluoguxiang Alley</h2>
                                <p>
                                    Located between Gulou East Street and Di'anmen East Street in Dongcheng District, it
                                    is the most intact existing courtyard complex of Yuan Dynasty hutongs in Beijing.
                                    Named for its north-south direction with Luoguxiang (Gong and Drum Alley) in the
                                    middle, its "chessboard-style" street pattern was established during the Yuan
                                    Dynasty and has been passed down for over 700 years. Sixteen traditional hutongs are
                                    distributed on the east and west sides, preserving historical relics such as Qi
                                    Baishi's Former Residence and Mao Dun's Former Residence. Today, it gathers more
                                    than 100 merchants including intangible cultural heritage handicraft workshops,
                                    independent bookstores, characteristic cultural and creative stores, and old Beijing
                                    snack shops. As an iconic block integrating old Beijing folk culture with modern
                                    trend creativity, it shows tourists the changes of hutong life from ancient times to
                                    the present.
                                </p>
                                <p>
                                    Opening Hours: Generally 9:00-17:00, some street-side merchants extend business
                                    hours to after 21:00. In case of special circumstances such as hutong maintenance,
                                    some areas may be temporarily closed—it is recommended to pay attention to official
                                    notifications in advance.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            Admission is free with no entrance fee. Some handicraft experience projects and
                            characteristic
                            exhibition halls in the block require separate payment, with prices ranging from 30 to 100
                            RMB
                            depending on the project.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Preferential Policies for Paid Projects: Most offer half-price tickets for children under
                            1.2
                            meters, with specific details subject to on-site announcements.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="nanluoguxiangChartContainer" id="nanluoguxiangChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (62% female, 38% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="nanluoguxiangPieChartContainer" id="nanluoguxiangPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 2% , individual 98% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="nanluoguxiangAgeChartContainer" id="nanluoguxiangAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 4%, 20-40: 66%, under 20: 30%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Well-Preserved Yuan Dynasty Hutong and Courtyard Texture
                                </h3>
                                <li>
                                    The block retains the original urban texture of Yuan Dynasty hutongs, with 16
                                    hutongs neatly
                                    arranged on the east and west sides, forming a fishbone-like layout. Walking through
                                    the
                                    lanes, you can see traditional courtyard houses (siheyuan) with gray tiles and white
                                    walls,
                                    experiencing the original hutong lifestyle and architectural aesthetics of old
                                    Beijing.
                                </li>
                                <h3></h3>
                                <h3>
                                    Famous Former Residences
                                </h3>
                                <li>
                                    There are many celebrity residences with profound historical heritage. The Prince
                                    Senggelinqin Mansion, once the residence of the prominent Qing Dynasty noble
                                    Senggelinqin,
                                    showcases the architectural style of Qing Dynasty noble mansions. Keyuan Garden (Ke
                                    Garden),
                                    once the residence and garden of Wen Yu, a grand secretary in the late Qing Dynasty,
                                    and
                                    Feng Guozhang, the acting president of the Republic of China, is regarded as the
                                    most
                                    artistically valuable private garden in Beijing during the late Qing Dynasty.
                                </li>
                                <!-- <h3></h3>
                                <h3>

                                </h3>
                                <li>

                                </li> -->

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 什刹海 -->
        <el-card class="document-list">
            <el-collapse v-model="shichahaiMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/shichahai_main.jpg" alt="shichahai"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Shichahai Lakes Area</h2>
                                <p>
                                    Located in the downtown area of Xicheng District, it consists of three connected
                                    water areas (Qianhai, Houhai, Xihai) and surrounding hutong blocks. Named for the
                                    ten temples around it in ancient times, it is the only open historical water area in
                                    Beijing’s inner city. Boating on the lake is available in summer, and an open-air
                                    ice rink is set up in winter. It perfectly integrates natural landscapes with
                                    cultural heritage, serving as a core area to experience the lifestyle of old
                                    Beijing.
                                </p>
                                <p>
                                    Opening Hours: The entire scenic area is open 24 hours a day. Individual attractions
                                    within the area have different opening hours. Some water activities may be suspended
                                    in case of extreme weather or water area maintenance—please check relevant
                                    information in advance.
                                </p>
                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            The scenic area is free of charge with no overall entrance fee. Separate tickets apply to
                            individual
                            attractions: Prince Gong’s Mansion (40 RMB per person), Soong Ching-ling’s Former Residence
                            (20 RMB
                            per person), Guo Moruo Memorial Hall (10 RMB per person).
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Free admission for children under 1.2 meters, seniors over 65 years old, and people with
                            disabilities (with valid documents); half-price tickets for children 1.2-1.4 meters tall and
                            full-time students with undergraduate or below academic qualifications (with valid
                            documents); free
                            admission for active military personnel (with valid documents).
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="shichahaiChartContainer" id="shichahaiChartContainer"
                                class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (49% female, 51% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="shichahaiPieChartContainer" id="shichahaiPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 15% , individual 85% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="shichahaiAgeChartContainer" id="shichahaiAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 33%, 20-40: 50%, under 20: 17%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Three Connected Lakes (Qianhai, Houhai, Xihai)
                                </h3>
                                <li>
                                    These three artificial lakes are lined with willow trees, boasting beautiful
                                    scenery. The
                                    shores are dotted with numerous bars, restaurants and characteristic shops, blending
                                    leisure
                                    atmosphere with old Beijing charm.
                                </li>
                                <h3></h3>
                                <h3>
                                    Prince Gong’s Mansion
                                </h3>
                                <li>
                                    A key attraction in the Shichahai area, it was once the residence of He Shen (a
                                    prominent
                                    minister of the Qing Dynasty) with extremely high architectural standards. Divided
                                    into the
                                    mansion and the garden, the garden’s "Three Wonders" are the Western-style Gate, the
                                    Grand
                                    Opera House and the Rear Covered Building.
                                </li>
                                <h3></h3>
                                <h3>
                                    Yandai Xiejie (Pipe Lane)
                                </h3>
                                <li>
                                    A highly distinctive street lined with traditional old Beijing snack shops and
                                    handicraft
                                    stores. It is also the location of "Yinding Guanshan" (Viewing Mountains from Silver
                                    Ingot
                                    Bridge), one of the "Eight Scenes of Yanjing".
                                </li>
                                <h3></h3>
                                <h3>
                                    Cultural Relics and Diverse Formats
                                </h3>
                                <li>
                                    The area preserves many cultural relic protection units such as Soong Ching-ling’s
                                    Former
                                    Residence and Guo Moruo Memorial Hall. It also gathers diverse businesses including
                                    old
                                    Beijing traditional snacks, folk song bars and characteristic homestays.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 军事博物馆 -->
        <el-card class="document-list">
            <el-collapse v-model="junboMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/junbo_main.jpg" alt="junbo" style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>The Military Museum of the Chinese People’s Revolution</h2>
                                <p>
                                    It is located on the western extension of Chang'an Avenue in Haidian District, and
                                    is China's only large - scale comprehensive military history museum. Officially
                                    opening to the public on October 1, 1959, the museum was designed by the renowned
                                    architect Zhang Kaiji. The main building stands 94.7 meters tall, with its design
                                    incorporating elements of "the Great Wall and gun barrels", symbolizing the iron
                                    Great Wall of the Chinese People's Liberation Army. It serves as a crucial venue for
                                    inheriting the red gene and popularizing military knowledge.
                                </p>
                                <p>
                                    Opening Hours: It is open from 9:00 to 17:00 from Tuesday to Sunday (admission
                                    closes at 16:00) and closed on Mondays (except for statutory holidays). The opening
                                    hours may be adjusted when major special exhibitions are held, and some exhibition
                                    halls might be temporarily closed for exhibit maintenance. It is advisable to check
                                    the latest information through official channels in advance.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            Admission is free but requires advance reservation. Visitors need to make reservations via
                            the
                            official WeChat official account 1 to 7 days ahead of their visit. However, some temporary
                            special
                            exhibitions may charge tickets, with prices usually ranging from 30 to 80 RMB per person.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Preferential Policies for Special Exhibitions: Half - price tickets are available for
                            students, the
                            elderly, and people with disabilities upon presentation of valid certificates.
                            Children under 1.2 meters in height are admitted free of charge (accompanied by an adult).
                            Active military personnel can enter for free with valid military IDs.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="junboChartContainer" id="junboChartContainer" class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (43% female, 57% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="junboPieChartContainer" id="junboPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 29% , individual 71% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="junboAgeChartContainer" id="junboAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 15%, 20-40: 63%, under 20: 22%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Ancient Weapons Hall
                                </h3>
                                <li>
                                    It systematically presents the evolution of Chinese weapons over thousands of years,
                                    from
                                    stone axes and bone spears of primitive society to bronze swords, iron spears, and
                                    crossbows
                                    of the Shang, Zhou, Qin, and Han dynasties. Highlights include exquisitely cast
                                    bronze
                                    ritual weapons from the Western Zhou Dynasty, sharp iron swords from the Warring
                                    States
                                    Period, and sophisticated siege equipment (such as trebuchets) from the Ming and
                                    Qing
                                    dynasties. These relics not only reflect the craftsmanship of ancient times but also
                                    reveal
                                    the strategic thinking of military operations in different eras.
                                </li>
                                <h3></h3>
                                <h3>
                                    Modern War Hall
                                </h3>
                                <li>
                                    Focusing on the period from the Opium War to the founding of New China, the hall
                                    uses
                                    cultural relics, historical photos, and scene restorations to vividly recount the
                                    Chinese
                                    nation’s struggle against foreign aggression and domestic revolutionary wars. Key
                                    exhibits
                                    include weapons used by the Taiping Rebellion army, military uniforms and badges of
                                    the
                                    Beiyang Army, firearms and documents from the War of Resistance against Japanese
                                    Aggression,
                                    and trophies seized from the Kuomintang army during the Liberation War. The scene
                                    restoration of the Long March and the display of the "Eight - Route Army’s 129th
                                    Division
                                    Headquarters" allow visitors to feel the arduousness of the revolutionary journey.
                                </li>
                                <h3></h3>
                                <h3>
                                    Contemporary Military Achievement Exhibition Areas
                                </h3>
                                <li>
                                    This is the most eye-catching part of the museum, showcasing China’s leapfrog
                                    development in
                                    national defense and military modernization. The outdoor exhibition area displays a
                                    large
                                    number of real large - scale weapons and equipment, such as fighter jets, bombers,
                                    tanks,
                                    armored vehicles, and warships, which can be viewed up close and photographed. The
                                    indoor
                                    hall features core exhibits including the Dongfeng - 5 intercontinental missile, the
                                    Dongfeng - 21D anti - ship ballistic missile, and a full - size model of the J - 20
                                    stealth
                                    fighter jet. In addition, the "Aerospace Military Exhibition Area" displays space -
                                    related
                                    military technologies and equipment, such as satellite models and space launch
                                    vehicles,
                                    reflecting the integration of aerospace and national defense.
                                </li>
                                <h3></h3>
                                <h3>
                                    Precious Historical Relics with Stories
                                </h3>
                                <li>
                                    There are many cultural relics with significant historical significance in the
                                    collection.
                                    The Hongqi CA72 sedan used by the central leaders during the founding ceremony in
                                    1949 is
                                    preserved intact, with every detail telling the glory of the founding of New China.
                                    The
                                    M4A3E8 "Sherman" tank seized by the Chinese People’s Volunteers during the War to
                                    Resist
                                    U.S. Aggression and Aid Korea bears the marks of war and is a witness to the
                                    volunteers’
                                    heroic struggle. In addition, the pistols used by revolutionary martyrs, the
                                    military maps
                                    marked with battle plans, and the letters written on the battlefield all carry
                                    profound
                                    historical memories, allowing visitors to connect with the past and cherish the
                                    present
                                    peace.
                                </li>
                                <h3></h3>
                                <h3>
                                    Thematic Permanent Halls
                                </h3>
                                <li>
                                    In addition to the above - mentioned halls, the museum has specialized permanent
                                    exhibitions
                                    such as "China’s Ancient Military History", "China’s Modern Military History", and
                                    "Achievements in National Defense and Army Building of New China". These halls adopt
                                    a
                                    combination of chronological order and thematic classification, supplemented by
                                    multimedia
                                    presentations such as sound, light, and video, to make the display more vivid and
                                    intuitive.
                                    For example, the "Military Science and Technology Exhibition Hall" explains the
                                    principles
                                    and applications of modern military technology through interactive exhibits, while
                                    the
                                    "Military Art Exhibition Hall" displays military paintings, sculptures, and
                                    calligraphy
                                    works, integrating art and military culture.
                                </li>

                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 798艺术区 -->
        <el-card class="document-list">
            <el-collapse v-model="yishuquMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/yishuqu_main.jpg" alt="yishuqu"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>798 Art Zone</h2>
                                <p>
                                    Located in Jiuxianqiao Sub-district, Chaoyang District, it was formerly the
                                    state-owned 798 Factory (Beijing North China Radio Joint Equipment Factory) built in
                                    1952. Since 2002, it has gradually transformed into an art zone, with unique
                                    Bauhaus-style factory buildings as the core carrier. These buildings adopt a "square
                                    box" design, combining practicality and aesthetic value. Today, it gathers more than
                                    400 galleries, art institutions, design studios, cultural and creative stores, and
                                    characteristic catering merchants. It regularly holds art exhibitions, music
                                    festivals, design weeks and other activities, becoming an iconic gathering place for
                                    Chinese contemporary art and trend culture, attracting art lovers and tourists from
                                    home and abroad.
                                </p>
                                <p>
                                    Opening Hours: The entire park is open 24 hours a day. Most galleries and exhibition
                                    halls in the zone are open from 10:00 to 19:00, and some stores are closed on
                                    Mondays. Temporary control may be implemented in some areas when large-scale
                                    activities are held—it is recommended to check activity information in advance.
                                </p>

                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>
                        <h2>Basic Ticket Prices</h2>
                        <p>
                            The park is free of charge with no entrance fee. Some special exhibitions in galleries and
                            art
                            institutions in the zone require separate payment, with prices usually ranging from 50 to
                            200 RMB
                            per person.
                        </p>
                        <h2>Preferential Policies</h2>
                        <p>
                            Most offer half-price tickets for students with student ID cards and free admission for
                            children
                            under 1.2 meters. Some exhibitions have fixed free opening days every month, with specific
                            details
                            subject to official announcements.
                        </p>

                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="yishuquChartContainer" id="yishuquChartContainer" class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (The current public research does not specify the latest overall
                                gender
                                ratio)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="yishuquPieChartContainer" id="yishuquPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 25% , individual 75% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="yishuquAgeChartContainer" id="yishuquAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 10%, 20-40: 80%, under 20: 10%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Bauhaus-Style Industrial Factory Buildings
                                </h3>
                                <li>
                                    These are the soul of 798 Art Zone. The original factory buildings, designed by East
                                    German
                                    architects in the 1950s, feature simple lines, large glass windows, and reinforced
                                    concrete
                                    structures—typical of the Bauhaus style that emphasizes functionality. After
                                    transformation
                                    by artists, the tall and spacious workshops have been reborn as galleries, art
                                    studios, and
                                    cultural companies. The contrast between the rough industrial texture (exposed
                                    concrete
                                    beams, rusty pipelines) and the delicate artworks creates a unique aesthetic
                                    experience,
                                    making every corner a photo-worthy spot.
                                </li>
                                <h3></h3>
                                <h3>
                                    Key Art Institutions
                                </h3>
                                <li>
                                    UCCA Center for Contemporary Art: One of China’s most influential contemporary art
                                    institutions, it hosts large-scale international exhibitions throughout the year,
                                    showcasing
                                    works by renowned artists from China and abroad. Its industrial-style exhibition
                                    space and
                                    cutting-edge curatorial concepts attract a large number of art enthusiasts.
                                </li>
                                <li>
                                    798 Art Center:Focusing on promoting domestic contemporary art, it regularly holds
                                    group
                                    exhibitions, solo shows, and academic seminars, covering painting, sculpture,
                                    installation,
                                    video, and other art forms.
                                </li>
                                <li>Other institutions such as galleries and design studios present diverse artistic
                                    expressions, from traditional art to experimental works, catering to different
                                    aesthetic
                                    needs.
                                </li>
                                <h3></h3>
                                <h3>
                                    798 Creative Square
                                </h3>
                                <li>
                                    As the core public space of the art zone, it is surrounded by iconic factory
                                    buildings and
                                    large-scale outdoor sculptures. It is the venue for major events such as music
                                    festivals,
                                    design weeks, and art fairs. On ordinary days, it is a gathering place for visitors
                                    to rest,
                                    communicate, and appreciate street art, with frequent impromptu performances and
                                    creative
                                    market activities.
                                </li>
                                <h3></h3>
                                <h3>
                                    Street Art & Public Artworks
                                </h3>
                                <li>
                                    The walls of the entire art zone are covered with colorful graffiti and murals
                                    created by
                                    artists from all over the world, each telling a unique story. Scattered across the
                                    park are
                                    various public sculptures—some are abstract and avant-garde, while others are
                                    playful and
                                    interactive. These artworks integrate with the industrial environment, turning the
                                    entire
                                    zone into an open-air art museum where art can be enjoyed anytime, anywhere.
                                </li>
                                <h3></h3>
                                <h3>
                                    Cultural and Creative Ecology
                                </h3>
                                <li>
                                    In addition to art exhibitions, 798 also gathers a large number of characteristic
                                    cultural
                                    and creative stores, handcraft workshops, and themed restaurants. You can buy
                                    original
                                    cultural and creative products, experience hand-making, or taste creative cuisine in
                                    industrial-style spaces. This integration of art, commerce, and life makes 798 not
                                    only an
                                    art exhibition venue but also a trendy destination for leisure and consumption.
                                </li>

                            </ul>

                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>

        <!-- 环球影城 -->
        <el-card class="document-list">
            <el-collapse v-model="huanqiuMianban">
                <el-collapse-item name="1">
                    <template #title>
                        <div class="panel-header">
                            <!-- 左边图片 -->
                            <div class="panel-image-container">
                                <img src="../../figure/huanqiu_main.jpg" alt="huanqiu"
                                    style="width: 100%; height: 100%;">

                            </div>
                            <!-- 右边文字 -->
                            <span class="panel-title">
                                <h2>Universal Studios Beijing (USJ)</h2>
                                <p>
                                    Located at the intersection of Beijing-Harbin Expressway and East Sixth Ring Road in
                                    Tongzhou District, it is the fifth Universal Studios theme park worldwide and the
                                    third in Asia. Officially opening on September 20, 2021, it is a joint venture
                                    between Universal Pictures (USA) and Beijing Tourism Group, covering an area of over
                                    4 square kilometers. Boasting seven themed lands, 37 rides and entertainment
                                    facilities, and 41 live shows, it is complemented by a catering and commercial
                                    district and themed hotels, serving as a large-scale resort integrating
                                    entertainment, dining, and accommodation.
                                </p>
                                <p>
                                    Opening Hours: Generally open from 10:00 to 21:00 (daily hours may vary slightly;
                                    extended to 22:00 on holidays). Some rides may be temporarily closed due to extreme
                                    weather or equipment maintenance—please check the daily operation information via
                                    the official APP in advance.
                                </p>
                            </span>
                        </div>
                    </template>
                    <div class="panel-content">
                        <h1>Ticket prices for </h1>

                        <table class="bordered-table">
                            <thead>
                                <tr>
                                    <th>Ticket Type</th>
                                    <th>Price</th>
                                    <th>Applicable Periods</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Off-Peak Day</td>
                                    <td>¥418</td>
                                    <td>Some spring and autumn dates, most winter dates</td>
                                </tr>
                                <tr>
                                    <td>Regular Day</td>
                                    <td>¥528</td>
                                    <td>Most spring and autumn dates, some winter dates</td>
                                </tr>
                                <tr>
                                    <td>Peak Day</td>
                                    <td>¥638</td>
                                    <td>Opening month, some Chinese statutory holidays, some summer dates, some spring
                                        and
                                        autumn dates</td>
                                </tr>
                                <tr>
                                    <td>Special Day</td>
                                    <td>¥748</td>
                                    <td>Some Chinese statutory holidays, most summer dates</td>
                                </tr>
                            </tbody>
                        </table>
                        <p>In addition, children aged 3-11 years old and seniors aged 65 years old and above are
                            eligible for
                            approximately a 25% discount. Infants under 3 years old are admitted free of charge.</p>

                        <h3>Multi-Day Combo Tickets</h3>
                        <table class="bordered-table">
                            <thead>
                                <tr>
                                    <th>Type</th>
                                    <th>Standard Ticket Price</th>
                                    <th>Discounted Ticket Price</th>
                                    <th>Remarks</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1.5-Day Ticket</td>
                                    <td>Starting from ¥670</td>
                                    <td>Starting from ¥505</td>
                                    <td>Discounted tickets apply to children aged 3-11 and seniors aged 65+; the ticket
                                        allows
                                        entry after 14:00 on the first day + full-day access on the second day</td>
                                </tr>
                                <tr>
                                    <td>2-Day Combo Ticket</td>
                                    <td>¥619 on online platforms (¥815.3 at the gate)</td>
                                    <td>No publicly unified discounted price</td>
                                    <td>The second entry can be used on any date from the day after the first entry up
                                        to the
                                        6th day after the first entry</td>
                                </tr>
                            </tbody>
                        </table>

                        <h3>Annual Passes</h3>
                        <table class="bordered-table">
                            <thead>
                                <tr>
                                    <th>Annual Pass Type</th>
                                    <th>Price</th>
                                    <th>Core Benefits</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Light Enjoy Annual Pass</td>
                                    <td>¥988</td>
                                    <td>183 admission days, applicable mainly on Mondays to Thursdays, and some Sundays
                                        in
                                        winter</td>
                                </tr>
                                <tr>
                                    <td>Leisure Enjoy Annual Pass</td>
                                    <td>¥1688</td>
                                    <td>227 admission days, adding Sundays in September-October and Fridays in
                                        November-December
                                        on the basis of the Light Enjoy Annual Pass</td>
                                </tr>
                                <tr>
                                    <td>Premium Enjoy Annual Pass</td>
                                    <td>¥2488</td>
                                    <td>303 admission days, covering more Sundays as well as Saturdays and Sundays in
                                        winter
                                    </td>
                                </tr>
                                <tr>
                                    <td>Exclusive Enjoy Annual Pass</td>
                                    <td>¥3588</td>
                                    <td>Unlimited reservation-based admission for 365 days, including holidays; also
                                        includes
                                        exclusive benefits such as 2 free Universal Single Express Passes per quarter
                                    </td>
                                </tr>
                                <tr>
                                    <td>College Student Annual Pass</td>
                                    <td>Fixed pricing not announced</td>
                                    <td>Bookable admission dates apply to most Mondays to Thursdays, catering to college
                                        students' leisure time and summer/winter vacation travel needs</td>
                                </tr>
                            </tbody>
                        </table>
                        <p>All annual pass holders can renew their passes 60 days before the expiration of the original
                            pass
                            validity period and enjoy a 10% discount on renewal. Except for the Exclusive Enjoy Annual
                            Pass,
                            other tiers of annual passes can be flexibly upgraded.</p>


                        <!-- 性别比例图表 -->
                        <div class="chart-section">
                            <h4>Distribution of tourist gender ratio</h4>
                            <div ref="huanqiuChartContainer" id="huanqiuChartContainer" class="pictorial-bar-container">
                                <!-- ECharts 将在此处渲染 -->
                            </div>
                            <div class="chart-footer">
                                * Gender distribution (55% female, 45% male)
                            </div>
                        </div>

                        <!-- 游客类型和年龄分布在同一行 -->
                        <div class="chart-row">
                            <!-- 游客类型饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Distribution of tourist types</h4>
                                <div ref="huanqiuPieChartContainer" id="huanqiuPieChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Distribution of tourist types (Team 80% , individual 20% )
                                </div>
                            </div>

                            <!-- 年龄分布饼图 -->
                            <div class="chart-section chart-half">
                                <h4>Age distribution</h4>
                                <div ref="huanqiuAgeChartContainer" id="huanqiuAgeChartContainer"
                                    class="pie-chart-container">
                                    <!-- ECharts 年龄饼图将在此处渲染 -->
                                </div>
                                <div class="chart-footer">
                                    * Age distribution (over 40: 20%, 20-40: 60%, under 20: 20%)
                                </div>
                            </div>
                        </div>

                        <div class="attraction-info">
                            <h1>Main Attractions</h1>
                            <ul>
                                <h3>
                                    Seven Themed Lands
                                </h3>
                                <li>
                                    <h4>
                                        The Wizarding World of Harry Potter
                                    </h4>
                                    <p>
                                        A highly immersive magic kingdom with Hogwarts Castle as the centerpiece. Wander
                                        through
                                        cobblestone streets of Hogsmeade Village, visit iconic spots like Ollivanders
                                        Wand Shop
                                        and Honeydukes. Experience the thrilling "Harry Potter and the Forbidden
                                        Journey" ride
                                        inside the castle, and watch the spectacular night projection show on the castle
                                        walls,
                                        fully embracing the magic from the books and films.
                                    </p>
                                </li>
                                <li>
                                    <h4>
                                        Transformers Metrobase
                                    </h4>
                                    <p>
                                        The world’s first Transformers-themed land, set in a top-secret N.E.S.T.
                                        headquarters.
                                        Featuring cyberpunk-style architecture and giant robot installations, it offers
                                        heart-pounding rides like "Transformers: Battle for the AllSpark" (a 3D dark
                                        ride) and
                                        high-speed roller coasters. The futuristic tech atmosphere makes visitors feel
                                        like
                                        they’re part of the Autobot-human alliance .
                                    </p>
                                </li>
                                <li>
                                    <h4>
                                        Kung Fu Panda Land of Awesomeness
                                    </h4>
                                    <p>
                                        The world’s first fully indoor Kung Fu Panda-themed land, brimming with
                                        Chinese-style
                                        charm. It recreates scenes from the animated films, including Jade Palace, Panda
                                        Village, and the Wisdom Peach Tree. Enjoy gentle rides like "Kung Fu Panda:
                                        Journey of
                                        the Dragon Warrior" and watch lively martial arts performances, with traditional
                                        Chinese
                                        architecture and festive decorations creating a warm, immersive experience .
                                    </p>
                                </li>
                                <li>
                                    <h4>
                                        Minion Land
                                    </h4>
                                    <p>
                                        A playful paradise based on the "Despicable Me" films. Meet mischievous Minions,
                                        ride
                                        the spinning "Minion Mayhem" attraction, and wander through colorful, whimsical
                                        streets.
                                        The area offers family-friendly shows and Minion-themed snacks, making it a hit
                                        with
                                        both kids and adults .
                                    </p>
                                </li>
                                <li>
                                    <h4>
                                        Jurassic World Isla Nublar
                                    </h4>
                                    <p>
                                        A prehistoric adventure land inspired by the "Jurassic World" movies. Come
                                        face-to-face
                                        with life-sized dinosaurs like T-Rex and Velociraptors. Experience the thrilling
                                        "Jurassic World Adventure" ride through dinosaur habitats, and explore lush
                                        jungles and
                                        scientific research facilities, blending excitement with educational elements .
                                    </p>
                                </li>
                                <li>
                                    <h4>
                                        Hollywood
                                    </h4>
                                    <p>
                                        A replica of Los Angeles’ Hollywood Boulevard, lined with palm trees and
                                        movie-themed
                                        storefronts. Don’t miss "Lights, Camera, Action!"—a film effects show co-created
                                        by
                                        Zhang Yimou and Steven Spielberg, showcasing stunning behind-the-scenes movie
                                        magic that
                                        combines Eastern and Western cultures .
                                    </p>
                                </li>
                                <li>
                                    <h4>
                                        WaterWorld
                                    </h4>
                                    <p>
                                        More than just a stunt show venue, it’s a fully themed land. Watch high-octane
                                        water
                                        battles with explosions, stunts, and aerial performances. The coastal-style
                                        scenery and
                                        themed restaurants offer a unique aquatic entertainment experience, being the
                                        first
                                        WaterWorld land in any Universal Studios resort .
                                    </p>
                                </li>

                                <h3></h3>
                                <h3>
                                    Supporting Facilities
                                </h3>
                                <li>
                                    <h4>
                                        Universal CityWalk Beijing
                                    </h4>
                                    <p>
                                        A vibrant commercial district outside the park, open to the public for free. It
                                        features
                                        over 100 dining, shopping, and entertainment outlets, including international
                                        restaurants, local snacks, and flagship stores, perfect for pre or post-park
                                        leisure.
                                    </p>
                                </li>
                                <li>
                                    <h4>
                                        Themed Hotels
                                    </h4>
                                    <p>
                                        Two on-site hotels—Universal Studios Grand Hotel (with movie-themed rooms and
                                        direct
                                        park access) and NUO Resort Hotel (blending Chinese elegance with luxury)—offer
                                        convenient accommodation and exclusive guest perks. </p>
                                </li>


                            </ul>
                        </div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </el-card>


    </div>
</template>

<script setup>
import { ref, reactive, onMounted, watch, nextTick } from "vue";
import { ElMessage } from "element-plus";
import * as echarts from 'echarts';

// 控制故宫折叠面板的展开状态
const gugongMianban = ref([]);

// 控制天坛折叠面板的展开状态
const tiantanMianban = ref([]);
const yiheyuanMianban = ref([]);
const yuanmingyuanMianban = ref([]);
const changchengMianban = ref([]);
const beihaiMianban = ref([]);
const yonghegongMianban = ref([]);
const guoboMianban = ref([]);
const niaochaoMianban = ref([]);
const shuilifangMianban = ref([]);
const xiangshanMianban = ref([]);
const nanluoguxiangMianban = ref([]);
const shichahaiMianban = ref([]);
const junboMianban = ref([]);
const yishuquMianban = ref([]);
const huanqiuMianban = ref([]);

// 图表实例引用
let gugongChart = null;
let tiantanChart = null;
let yiheyuanChart = null;
let yuanmingyuanChart = null;
let changchengChart = null;
let beihaiChart = null;
let yonghegongChart = null;
let guoboChart = null;
let niaochaoChart = null;
let shuilifangChart = null;
let xiangshanChart = null;
let nanluoguxiangChart = null;
let shichahaiChart = null;
let junboChart = null;
let yishuquChart = null;
let huanqiuChart = null;

let gugongPieChart = null;
let tiantanPieChart = null;
let yiheyuanPieChart = null;
let yuanmingyuanPieChart = null;
let changchengPieChart = null;
let beihaiPieChart = null;
let yonghegongPieChart = null;
let guoboPieChart = null;
let niaochaoPieChart = null;
let shuilifangPieChart = null;
let xiangshanPieChart = null;
let nanluoguxiangPieChart = null;
let shichahaiPieChart = null;
let junboPieChart = null;
let yishuquPieChart = null;
let huanqiuPieChart = null;

let gugongAgeChart = null;
let tiantanAgeChart = null;
let yiheyuanAgeChart = null;
let yuanmingyuanAgeChart = null;
let changchengAgeChart = null;
let beihaiAgeChart = null;
let yonghegongAgeChart = null;
let guoboAgeChart = null;
let niaochaoAgeChart = null;
let shuilifangAgeChart = null;
let xiangshanAgeChart = null;
let nanluoguxiangAgeChart = null;
let shichahaiAgeChart = null;
let junboAgeChart = null;
let yishuquAgeChart = null;
let huanqiuAgeChart = null;

// 添加获取figure目录下图片的方法
const getFigureImageSrc = (filename) => {
    try {
        return new URL(`../../figure/${filename}`, import.meta.url).href;
    } catch (error) {
        console.warn(`图片 ../../figure/${filename} 未找到`);
        return '';
    }
};

// 定义figure目录下的图片数据
const figureImages = ref([
    {
        id: 1,
        src: getFigureImageSrc('gugong.jpg'),
        alt: 'Gugong'
    },
    {
        id: 2,
        src: getFigureImageSrc('tiantan.jpg'),
        alt: 'Tiantan'
    },
    {
        id: 3,
        src: getFigureImageSrc('yiheyuan.jpg'),
        alt: 'Yiheyuan'
    },
    {
        id: 4,
        src: getFigureImageSrc('yuanmingyuan.jpg'),
        alt: 'Yuanmingyuan'
    },
    {
        id: 5,
        src: getFigureImageSrc('changcheng.jpg'),
        alt: 'Changcheng'
    },
    {
        id: 6,
        src: getFigureImageSrc('beihai.jpg'),
        alt: 'Beihai'
    },
    {
        id: 7,
        src: getFigureImageSrc('yonghegong.jpg'),
        alt: 'Yonghegong'
    },
    {
        id: 8,
        src: getFigureImageSrc('guobo.jpg'),
        alt: 'Guobo'
    },
    {
        id: 9,
        src: getFigureImageSrc('niaochao.jpg'),
        alt: 'Niaochao'
    },
    {
        id: 10,
        src: getFigureImageSrc('shuilifang.jpg'),
        alt: 'Shuilifang'
    },
    {
        id: 11,
        src: getFigureImageSrc('xiangshan.jpg'),
        alt: 'Xiangshan'
    },
    {
        id: 12,
        src: getFigureImageSrc('nanluoguxiang.jpg'),
        alt: 'Nanluoguxiang'
    },
    {
        id: 13,
        src: getFigureImageSrc('shichahai.jpg'),
    },
    {
        id: 14,
        src: getFigureImageSrc('junbo.jpg'),
        alt: 'Junbo'
    },
    {
        id: 15,
        src: getFigureImageSrc('yishuqu.jpg'),
        alt: 'Yishuqu'
    },
    {
        id: 16,
        src: getFigureImageSrc('huanqiu.jpg'),
        alt: 'Huanqiu'
    }

    // ... 其他图片数据保持不变
]);

/**
 * 初始化性别比例象形柱状图（复用函数）
 * @param {string} chartContainerId - 图表容器的ID
 * @param {number} femalePercent - 女性比例
 * @param {number} malePercent - 男性比例
 * @param {string} chartName - 图表名称（用于日志和错误处理）
 * @param {Object} chartInstanceRef - 图表实例的引用
 * @returns {Object} - 图表实例
 */
const initGenderRatioChart = (chartContainerId, femalePercent, malePercent, chartName, chartInstanceRef) => {
    // 先销毁已有实例
    if (chartInstanceRef.value) {
        chartInstanceRef.value.dispose();
        chartInstanceRef.value = null;
    }

    // 使用nextTick确保DOM更新完成
    nextTick(() => {
        const chartDom = document.getElementById(chartContainerId);
        if (!chartDom) {
            console.warn(`${chartName}图表容器未找到`);
            return;
        }

        // 确保容器有明确的尺寸
        chartDom.style.height = '400px';
        chartDom.style.width = '100%';

        try {
            const chart = echarts.init(chartDom);

            // 构造系列数据（交替插入空值）
            const femaleSeriesData = [];
            const maleSeriesData = [];

            femaleSeriesData.push(femalePercent);
            femaleSeriesData.push('-'); // 女性行的男性数据为空
            maleSeriesData.push('-'); // 男性行的女性数据为空
            maleSeriesData.push(malePercent);

            const option = {
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    },
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
                    textStyle: {
                        color: '#606266'
                    }
                },
                grid: {
                    left: '10%',
                    right: '10%',
                    bottom: '10%',
                    top: '15%',
                    containLabel: true
                },
                xAxis: {
                    type: 'value',
                    name: 'Percentage (%)',
                    nameTextStyle: {
                        color: '#606266'
                    },
                    axisLabel: {
                        color: '#606266',
                        fontSize: 12
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#ddd'
                        }
                    },
                    splitLine: {
                        lineStyle: {
                            color: '#eee'
                        }
                    },
                    max: 100
                },
                yAxis: {
                    type: 'category',
                    data: chartName == ['Female', 'Male'],
                    axisLabel: {
                        color: '#606266',
                        fontSize: 14,
                        lineHeight: 20
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#ddd'
                        }
                    }
                },
                series: [
                    {
                        name: 'Female proportion',
                        type: 'pictorialBar',
                        data: femaleSeriesData,
                        symbol: 'path://M693.064905 504.590142l-55.845778-202.954549c-7.532724-22.967796-34.488553-63.372358-79.685923-65.239925h-89.777337c-46.750604 1.927976-73.520086 41.894316-80.000256 65.365863l-55.777177 202.707792c-11.954885 44.266658 39.220951 61.57032 51.857744 19.985218l49.867311-187.020846h14.008799l-85.85176 328.529989h80.247012v246.909946c0 44.697714 60.764522 44.697714 60.764522 0v-246.909946h18.924473v246.909946c0 44.697714 58.766922 44.697714 58.766922 0v-246.909946h82.427888l-87.654823-328.529989h15.938823l49.988129 187.020846c12.331675 42.517862 63.256659 24.280417 51.801431-19.864399zM512.336858 219.833299c38.471467 0 69.538196-32.435663 69.538196-72.527941 0-40.031868-31.066729-72.528965-69.538196-72.528965-38.415154 0-69.48393 32.497096-69.48393 72.528965 0 40.030845 31.0698 72.527941 69.48393 72.527941z',
                        symbolSize: [20, 20],
                        symbolMargin: 2,
                        symbolRepeat: true,
                        symbolRepeatDirection: 'start',
                        symbolClip: true,
                        symbolBoundingData: 100,
                        symbolPosition: 'start',
                        itemStyle: {
                            color: '#d37a90'
                        },
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
                        name: 'Male proportion',
                        type: 'pictorialBar',
                        data: maleSeriesData,
                        symbol: 'path://M516.608 217.6c40.448 0 72.704-32.768 72.704-72.704 0-40.448-32.768-72.704-72.704-72.704-40.448 0-72.704 32.768-72.704 72.704s32.256 72.704 72.704 72.704z m80.384 18.432H435.712c-51.2 0-93.696 41.472-93.696 93.184v225.28c0 17.408 13.824 31.744 31.232 31.744s31.744-14.336 31.744-31.744V351.744h16.384v565.76c0 23.552 18.944 42.496 43.008 42.496 23.552 0 42.496-18.944 42.496-42.496V588.8h17.408v328.192c0 23.552 18.944 42.496 42.496 42.496 23.552 0 43.008-18.944 43.008-42.496V351.744h16.384v203.264c0 17.408 14.336 31.744 31.744 31.744 17.408 0 31.232-14.336 31.232-31.744v-225.28c1.024-51.712-40.96-93.696-92.16-93.696z',
                        symbolSize: [20, 20],
                        symbolMargin: 2,
                        symbolRepeat: true,
                        symbolRepeatDirection: 'start',
                        symbolClip: true,
                        symbolBoundingData: 100,
                        symbolPosition: 'start',
                        itemStyle: {
                            color: '#5470c6'
                        },
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
                animationDuration: 1000,
                animationEasing: 'cubicOut'
            };

            chart.setOption(option);

            // 监听窗口大小变化
            const resizeHandler = () => {
                if (chart && !chart.isDisposed()) {
                    chart.resize();
                }
            };
            window.addEventListener('resize', resizeHandler);

            // 保存图表实例到引用
            chartInstanceRef.value = chart;

            console.log(`${chartName}象形柱状图初始化成功`);

            return chart;

        } catch (error) {
            console.error(`${chartName}图表初始化失败:`, error);
            initFallbackChart(chartDom, [femalePercent, malePercent], chartName, chartInstanceRef);
        }
    });
};

/**
 * 初始化游客类型饼图（复用函数）
 * @param {string} chartContainerId - 图表容器的ID
 * @param {number} teamPercent - 团队比例
 * @param {number} individualPercent - 散客比例
 * @param {string} chartName - 图表名称（用于日志和错误处理）
 * @param {Object} chartInstanceRef - 图表实例的引用
 * @returns {Object} - 图表实例
 */
const initTouristTypePieChart = (chartContainerId, teamPercent, individualPercent, chartName, chartInstanceRef) => {
    // 先销毁已有实例
    if (chartInstanceRef.value) {
        chartInstanceRef.value.dispose();
        chartInstanceRef.value = null;
    }

    // 使用nextTick确保DOM更新完成
    nextTick(() => {
        const chartDom = document.getElementById(chartContainerId);
        if (!chartDom) {
            console.warn(`${chartName}饼图容器未找到`);
            return;
        }

        // 确保容器有明确的尺寸
        chartDom.style.height = '400px';
        chartDom.style.width = '100%';

        try {
            const chart = echarts.init(chartDom);

            // const isGugong = chartName === '故宫';
            const teamText = 'Team';
            const individualText = 'Individual';

            const option = {
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c}% ({d}%)'
                },
                legend: {
                    orient: 'horizontal',
                    bottom: '0%',
                    data: [teamText, individualText],
                    textStyle: {
                        color: '#606266',
                        fontSize: 14
                    }
                },
                series: [
                    {
                        name: 'Tourist Type',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        center: ['50%', '45%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: true,
                            formatter: '{b}: {c}%',
                            fontSize: 14,
                            fontWeight: 'bold'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 16,
                                fontWeight: 'bold'
                            },
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        },
                        labelLine: {
                            show: true
                        },
                        data: [
                            {
                                value: teamPercent,
                                name: teamText,
                                itemStyle: {
                                    color: '#91cc75' // 团队颜色 - 绿色
                                }
                            },
                            {
                                value: individualPercent,
                                name: individualText,
                                itemStyle: {
                                    color: '#fac858' // 散客颜色 - 黄色
                                }
                            }
                        ],
                        animation: true,
                        animationDuration: 1000,
                        animationEasing: 'cubicOut'
                    }
                ]
            };

            chart.setOption(option);

            // 监听窗口大小变化
            const resizeHandler = () => {
                if (chart && !chart.isDisposed()) {
                    chart.resize();
                }
            };
            window.addEventListener('resize', resizeHandler);

            // 保存图表实例到引用
            chartInstanceRef.value = chart;

            console.log(`${chartName}游客类型饼图初始化成功`);

            return chart;

        } catch (error) {
            console.error(`${chartName}饼图初始化失败:`, error);
            return null;
        }
    });
};

/**
 * 初始化年龄分布饼图
 * @param {string} chartContainerId - 图表容器的ID
 * @param {number} over40Percent - 40岁以上比例
 * @param {number} age20to40Percent - 20-40岁比例
 * @param {number} under20Percent - 20岁以下比例
 * @param {string} chartName - 图表名称（用于日志和错误处理）
 * @param {Object} chartInstanceRef - 图表实例的引用
 * @returns {Object} - 图表实例
 */
const initAgeDistributionChart = (chartContainerId, over40Percent, age20to40Percent, under20Percent, chartName, chartInstanceRef) => {
    // 先销毁已有实例
    if (chartInstanceRef.value) {
        chartInstanceRef.value.dispose();
        chartInstanceRef.value = null;
    }

    // 使用nextTick确保DOM更新完成
    nextTick(() => {
        const chartDom = document.getElementById(chartContainerId);
        if (!chartDom) {
            console.warn(`${chartName}年龄饼图容器未找到`);
            return;
        }

        // 确保容器有明确的尺寸
        chartDom.style.height = '400px';
        chartDom.style.width = '100%';

        try {
            const chart = echarts.init(chartDom);

            // const isGugong = chartName === '故宫';

            const option = {
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c}% ({d}%)'
                },
                legend: {
                    orient: 'horizontal',
                    bottom: '0%',
                    data: [
                        'Over 40',
                        '20-40',
                        'Under 20'
                    ],
                    textStyle: {
                        color: '#606266',
                        fontSize: 14
                    }
                },
                series: [
                    {
                        name: 'Age Distribution',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        center: ['50%', '45%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: true,
                            formatter: '{b}: {c}%',
                            fontSize: 14,
                            fontWeight: 'bold'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 16,
                                fontWeight: 'bold'
                            },
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        },
                        labelLine: {
                            show: true
                        },
                        data: [
                            {
                                value: over40Percent,
                                name: 'Over 40',
                                itemStyle: {
                                    color: '#5470c6' // 蓝色
                                }
                            },
                            {
                                value: age20to40Percent,
                                name: '20-40',
                                itemStyle: {
                                    color: '#91cc75' // 绿色
                                }
                            },
                            {
                                value: under20Percent,
                                name: 'Under 20',
                                itemStyle: {
                                    color: '#fac858' // 黄色
                                }
                            }
                        ],
                        animation: true,
                        animationDuration: 1000,
                        animationEasing: 'cubicOut'
                    }
                ]
            };

            chart.setOption(option);

            // 监听窗口大小变化
            const resizeHandler = () => {
                if (chart && !chart.isDisposed()) {
                    chart.resize();
                }
            };
            window.addEventListener('resize', resizeHandler);

            // 保存图表实例到引用
            chartInstanceRef.value = chart;

            console.log(`${chartName}年龄分布饼图初始化成功`);

            return chart;

        } catch (error) {
            console.error(`${chartName}年龄饼图初始化失败:`, error);
            return null;
        }
    });
};

// 初始化故宫性别比例象形柱状图
const initGugongChart = () => {
    initGenderRatioChart('gugongChartContainer', 56, 44, '故宫', { value: gugongChart });
};

// 初始化天坛性别比例象形柱状图
const initTiantanChart = () => {
    initGenderRatioChart('tiantanChartContainer', 56, 44, '天坛', { value: tiantanChart });
};

// 初始化颐和园性别比例象形柱状图
const initYiheyuanChart = () => {
    initGenderRatioChart('yiheyuanChartContainer', 54, 46, '颐和园', { value: yiheyuanChart });
};

//圆明园性别比例象形柱状图
const initYuanmingyuanChart = () => {
    initGenderRatioChart('yuanmingyuanChartContainer', 52, 48, '圆明园', { value: yuanmingyuanChart });
};

// 初始化长城性别比例象形柱状图
const initChangchengChart = () => {
    initGenderRatioChart('changchengChartContainer', 50, 50, '八达岭长城', { value: changchengChart });
};

// 初始化北海公园性别比例象形柱状图
const initBeihaiChart = () => {
    initGenderRatioChart('beihaiChartContainer', 55, 45, '北海公园', { value: beihaiChart });
};

// 雍和宫性别比例象形柱状图
const initYonghegongChart = () => {
    initGenderRatioChart('yonghegongChartContainer', 65, 35, '雍和宫', { value: yonghegongChart });
};

// 国博性别比例象形柱状图
const initGuoboChart = () => {
    initGenderRatioChart('guoboChartContainer', 55, 45, '国家博物馆', { value: guoboChart });
};

// 鸟巢性别比例象形柱状图
const initNiaochaoChart = () => {
    initGenderRatioChart('niaochaoChartContainer', 45, 55, '鸟巢', { value: niaochaoChart });
};

// 水立方性别比例象形柱状图
const initShuilifangChart = () => {
    initGenderRatioChart('shuilifangChartContainer', 52, 48, '水立方', { value: shuilifangChart });
};

// 香山公园性别比例象形柱状图
const initXiangshanChart = () => {
    initGenderRatioChart('xiangshanChartContainer', 58, 42, '香山公园', { value: xiangshanChart });
};

// 南锣鼓巷性别比例象形柱状图
const initNanluoguxiangChart = () => {
    initGenderRatioChart('nanluoguxiangChartContainer', 62, 38, '南锣鼓巷', { value: nanluoguxiangChart });
};

// 什刹海性别比例象形柱状图
const initShichahaiChart = () => {
    initGenderRatioChart('shichahaiChartContainer', 48, 52, '什刹海', { value: shichahaiChart });
};

// 军博性别比例象形柱状图
const initJunboChart = () => {
    initGenderRatioChart('junboChartContainer', 43, 57, '军博', { value: junboChart });
};

// 艺术区性别比例象形柱状图
const initYishuquChart = () => {
    initGenderRatioChart('yishuquChartContainer', 50, 50, '艺术区', { value: yishuquChart });
};

// 环球性别比例象形柱状图
const initHuanqiuChart = () => {
    initGenderRatioChart('huanqiuChartContainer', 55, 45, '环球', { value: huanqiuChart });
};

//=======================================================================================================================
// 初始化故宫游客类型饼图
const initGugongPieChart = () => {
    initTouristTypePieChart('gugongPieChartContainer', 55, 45, '故宫', { value: gugongPieChart });
};

// 初始化天坛游客类型饼图
const initTiantanPieChart = () => {
    initTouristTypePieChart('tiantanPieChartContainer', 40, 60, '天坛', { value: tiantanPieChart });
};

// 初始化颐和园游客类型饼图
const initYiheyuanPieChart = () => {
    initTouristTypePieChart('yiheyuanPieChartContainer', 35, 65, '颐和园', { value: yiheyuanPieChart });
};

// 初始化圆明园游客类型饼图
const initYuanmingyuanPieChart = () => {
    initTouristTypePieChart('yuanmingyuanPieChartContainer', 30, 70, '圆明园', { value: yuanmingyuanPieChart });
};

// 初始化长城游客类型饼图
const initChangchengPieChart = () => {
    initTouristTypePieChart('changchengPieChartContainer', 60, 40, '八达岭长城', { value: changchengPieChart });
};

// 初始化北海公园游客类型饼图
const initBeihaiPieChart = () => {
    initTouristTypePieChart('beihaiPieChartContainer', 45, 55, '北海公园', { value: beihaiPieChart });
};

// 初始化雍和宫游客类型饼图
const initYonghegongPieChart = () => {
    initTouristTypePieChart('yonghegongPieChartContainer', 30, 70, '雍和宫', { value: yonghegongPieChart });
};

// 初始化国博游客类型饼图
const initGuoboPieChart = () => {
    initTouristTypePieChart('guoboPieChartContainer', 50, 50, '国家博物馆', { value: guoboPieChart });
};

// 初始化鸟巢游客类型饼图
const initNiaochaoPieChart = () => {
    initTouristTypePieChart('niaochaoPieChartContainer', 20, 80, '鸟巢', { value: niaochaoPieChart });
};

// 初始化水立方游客类型饼图
const initShuilifangPieChart = () => {
    initTouristTypePieChart('shuilifangPieChartContainer', 25, 75, '水立方', { value: shuilifangPieChart });
};

// 初始化香山公园游客类型饼图
const initXiangshanPieChart = () => {
    initTouristTypePieChart('xiangshanPieChartContainer', 30, 70, '香山公园', { value: xiangshanPieChart });
};

// 初始化南锣鼓巷游客类型饼图
const initNanluoguxiangPieChart = () => {
    initTouristTypePieChart('nanluoguxiangPieChartContainer', 2, 98, '南锣鼓巷', { value: nanluoguxiangPieChart });
};

// 初始化什刹海游客类型饼图
const initShichahaiPieChart = () => {
    initTouristTypePieChart('shichahaiPieChartContainer', 15, 85, '什刹海', { value: shichahaiPieChart });
};

// 初始化军博游客类型饼图
const initJunboPieChart = () => {
    initTouristTypePieChart('junboPieChartContainer', 29, 71, '军博', { value: junboPieChart });
};

// 初始化艺术区游客类型饼图
const initYishuquPieChart = () => {
    initTouristTypePieChart('yishuquPieChartContainer', 25, 75, '艺术区', { value: yishuquPieChart });
};

// 初始化环球游客类型饼图
const initHuanqiuPieChart = () => {
    initTouristTypePieChart('huanqiuPieChartContainer', 80, 20, '环球', { value: huanqiuPieChart });
};

//========================================================================================================================

// 初始化故宫年龄分布饼图
const initGugongAgeChart = () => {
    initAgeDistributionChart('gugongAgeChartContainer', 54, 31, 15, '故宫', { value: gugongAgeChart });
};

// 初始化天坛年龄分布饼图
const initTiantanAgeChart = () => {
    initAgeDistributionChart('tiantanAgeChartContainer', 50, 40, 10, '天坛', { value: tiantanAgeChart });
};

// 颐和园年龄分布饼图
const initYiheyuanAgeChart = () => {
    initAgeDistributionChart('yiheyuanAgeChartContainer', 45, 40, 15, '颐和园', { value: yiheyuanAgeChart });
};

// 圆明园年龄分布饼图
const initYuanmingyuanAgeChart = () => {
    initAgeDistributionChart('yuanmingyuanAgeChartContainer', 55, 35, 10, '圆明园', { value: yuanmingyuanAgeChart });
};

// 长城年龄分布饼图
const initChangchengAgeChart = () => {
    initAgeDistributionChart('changchengAgeChartContainer', 30, 50, 20, '八达岭长城', { value: changchengAgeChart });
};

// 北海公园年龄分布饼图
const initBeihaiAgeChart = () => {
    initAgeDistributionChart('beihaiAgeChartContainer', 40, 40, 20, '北海公园', { value: beihaiAgeChart });
};

// 雍和宫年龄分布饼图
const initYonghegongAgeChart = () => {
    initAgeDistributionChart('yonghegongAgeChartContainer', 70, 24, 6, '雍和宫', { value: yonghegongAgeChart });
};

// 国博年龄分布饼图
const initGuoboAgeChart = () => {
    initAgeDistributionChart('guoboAgeChartContainer', 38, 42, 20, '国家博物馆', { value: guoboAgeChart });
};

// 鸟巢年龄分布饼图
const initNiaochaoAgeChart = () => {
    initAgeDistributionChart('niaochaoAgeChartContainer', 17, 58, 25, '鸟巢', { value: niaochaoAgeChart });
};

// 水立方年龄分布饼图
const initShuilifangAgeChart = () => {
    initAgeDistributionChart('shuilifangAgeChartContainer', 15, 35, 40, '水立方', { value: shuilifangAgeChart });
};

// 香山公园年龄分布饼图
const initXiangshanAgeChart = () => {
    initAgeDistributionChart('xiangshanAgeChartContainer', 23, 73, 4, '香山公园', { value: xiangshanAgeChart });
};

// 南锣鼓巷年龄分布饼图
const initNanluoguxiangAgeChart = () => {
    initAgeDistributionChart('nanluoguxiangAgeChartContainer', 4, 66, 30, '南锣鼓巷', { value: nanluoguxiangAgeChart });
};

// 什刹海年龄分布饼图
const initShichahaiAgeChart = () => {
    initAgeDistributionChart('shichahaiAgeChartContainer', 33, 50, 17, '什刹海', { value: shichahaiAgeChart });
};

// 军博年龄分布饼图
const initJunboAgeChart = () => {
    initAgeDistributionChart('junboAgeChartContainer', 15, 63, 22, '军博', { value: junboAgeChart });
};

// 艺术区年龄分布饼图
const initYishuquAgeChart = () => {
    initAgeDistributionChart('yishuquAgeChartContainer', 10, 80, 10, '艺术区', { value: yishuquAgeChart });
};

// 环球年龄分布饼图
const initHuanqiuAgeChart = () => {
    initAgeDistributionChart('huanqiuAgeChartContainer', 20, 60, 20, '环球', { value: huanqiuAgeChart });
};

//========================================================================================================================
// 备用方案：普通柱状图
const initFallbackChart = (chartDom, data, name, chartInstanceRef) => {
    try {
        const chart = echarts.init(chartDom);

        const option = {
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                show: true,
                top: 'top'
            },
            xAxis: {
                type: 'category',
                data: name === '故宫' ? ['Female', 'Male'] : ['女性', '男性']
            },
            yAxis: {
                type: 'value',
                max: 100
            },
            series: [{
                name: name === '故宫' ? 'Gender Ratio' : '性别比例',
                type: 'bar',
                data: data,
                itemStyle: {
                    color: function (params) {
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

        chart.setOption(option);
        console.log(`${name}备用柱状图初始化成功`);

        // 保存图表实例到引用
        chartInstanceRef.value = chart;

        return chart;
    } catch (error) {
        console.error(`${name}备用图表也初始化失败:`, error);
        return null;
    }
};

// 监听故宫折叠面板状态变化
watch(gugongMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initGugongChart();
            initGugongPieChart();
            initGugongAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (gugongChart) {
            gugongChart.dispose();
            gugongChart = null;
        }
        if (gugongPieChart) {
            gugongPieChart.dispose();
            gugongPieChart = null;
        }
        if (gugongAgeChart) {
            gugongAgeChart.dispose();
            gugongAgeChart = null;
        }
    }
});

// 监听天坛折叠面板状态变化
watch(tiantanMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initTiantanChart();
            initTiantanPieChart();
            initTiantanAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (tiantanChart) {
            tiantanChart.dispose();
            tiantanChart = null;
        }
        if (tiantanPieChart) {
            tiantanPieChart.dispose();
            tiantanPieChart = null;
        }
        if (tiantanAgeChart) {
            tiantanAgeChart.dispose();
            tiantanAgeChart = null;
        }
    }
});

// 监听颐和园折叠面板状态变化
watch(yiheyuanMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initYiheyuanChart();
            initYiheyuanPieChart();
            initYiheyuanAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (yiheyuanChart) {
            yiheyuanChart.dispose();
            yiheyuanChart = null;
        }
        if (yiheyuanPieChart) {
            yiheyuanPieChart.dispose();
            yiheyuanPieChart = null;
        }
        if (yiheyuanAgeChart) {
            yiheyuanAgeChart.dispose();
            yiheyuanAgeChart = null;
        }
    }
});

// 监听圆明园折叠面板状态变化
watch(yuanmingyuanMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initYuanmingyuanChart();
            initYuanmingyuanPieChart();
            initYuanmingyuanAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (yuanmingyuanChart) {
            yuanmingyuanChart.dispose();
            yuanmingyuanChart = null;
        }
        if (yuanmingyuanPieChart) {
            yuanmingyuanPieChart.dispose();
            yuanmingyuanPieChart = null;
        }
        if (yuanmingyuanAgeChart) {
            yuanmingyuanAgeChart.dispose();
        }
    }
})

// 监听长城折叠面板状态变化
watch(changchengMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initChangchengChart();
            initChangchengPieChart();
            initChangchengAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (changchengChart) {
            changchengChart.dispose();
            changchengChart = null;
        }
        if (changchengPieChart) {
            changchengPieChart.dispose();
            changchengPieChart = null;
        }
        if (changchengAgeChart) {
            changchengAgeChart.dispose();
            changchengAgeChart = null;
        }
    }
})

// 监听北海公园折叠面板状态变化
watch(beihaiMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initBeihaiChart();
            initBeihaiPieChart();
            initBeihaiAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (beihaiChart) {
            beihaiChart.dispose();
            beihaiChart = null;
        }
        if (beihaiPieChart) {
            beihaiPieChart.dispose();
            beihaiPieChart = null;
        }
        if (beihaiAgeChart) {
            beihaiAgeChart.dispose();
        }
    }
})

// 监听雍和宫折叠面板状态变化
watch(yonghegongMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initYonghegongChart();
            initYonghegongPieChart();
            initYonghegongAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (yonghegongChart) {
            yonghegongChart.dispose();
            yonghegongChart = null;
        }
        if (yonghegongPieChart) {
            yonghegongPieChart.dispose();
            yonghegongPieChart = null;
        }
        if (yonghegongAgeChart) {
            yonghegongAgeChart.dispose();
            yonghegongAgeChart = null;
        }
    }
})

// 监听国博折叠面板状态变化
watch(guoboMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initGuoboChart();
            initGuoboPieChart();
            initGuoboAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (guoboChart) {
            guoboChart.dispose();
            guoboChart = null;
        }
        if (guoboPieChart) {
            guoboPieChart.dispose();
            guoboPieChart = null;
        }
        if (guoboAgeChart) {
            guoboAgeChart.dispose();
            guoboAgeChart = null;
        }
    }
});

// 监听鸟巢折叠面板状态变化
watch(niaochaoMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initNiaochaoChart();
            initNiaochaoPieChart();
            initNiaochaoAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (niaochaoChart) {
            niaochaoChart.dispose();
            niaochaoChart = null;
        }
        if (niaochaoPieChart) {
            niaochaoPieChart.dispose();
            niaochaoPieChart = null;
        }
        if (niaochaoAgeChart) {
            niaochaoAgeChart.dispose();
            niaochaoAgeChart = null;
        }
    }
})

// 监听水立方折叠面板状态变化
watch(shuilifangMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initShuilifangChart();
            initShuilifangPieChart();
            initShuilifangAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (shuilifangChart) {
            shuilifangChart.dispose();
            shuilifangChart = null;
        }
        if (shuilifangPieChart) {
            shuilifangPieChart.dispose();
            shuilifangPieChart = null;
        }
        if (shuilifangAgeChart) {
            shuilifangAgeChart.dispose();
            shuilifangAgeChart = null;
        }
    }
})

// 监听香山公园折叠面板状态变化
watch(xiangshanMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initXiangshanChart();
            initXiangshanPieChart();
            initXiangshanAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (xiangshanChart) {
            xiangshanChart.dispose();
            xiangshanChart = null;
        }
        if (xiangshanPieChart) {
            xiangshanPieChart.dispose();
            xiangshanPieChart = null;
        }
        if (xiangshanAgeChart) {
            xiangshanAgeChart.dispose();
            xiangshanAgeChart = null;
        }
    }
})

// 监听南锣鼓巷折叠面板状态变化
watch(nanluoguxiangMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initNanluoguxiangChart();
            initNanluoguxiangPieChart();
            initNanluoguxiangAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (nanluoguxiangChart) {
            nanluoguxiangChart.dispose();
            nanluoguxiangChart = null;
        }
        if (nanluoguxiangPieChart) {
            nanluoguxiangPieChart.dispose();
            nanluoguxiangPieChart = null;
        }
        if (nanluoguxiangAgeChart) {
            nanluoguxiangAgeChart.dispose();
            nanluoguxiangAgeChart = null;
        }

    }
})

// 监听什刹海折叠面板状态变化
watch(shichahaiMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initShichahaiChart();
            initShichahaiPieChart();
            initShichahaiAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (shichahaiChart) {
            shichahaiChart.dispose();
            shichahaiChart = null;
        }
        if (shichahaiPieChart) {
            shichahaiPieChart.dispose();
            shichahaiPieChart = null;
        }
        if (shichahaiAgeChart) {
            shichahaiAgeChart.dispose();
            shichahaiAgeChart = null;
        }
    }
})

// 监听军博折叠面板状态变化
watch(junboMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initJunboChart();
            initJunboPieChart();
            initJunboAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (junboChart) {
            junboChart.dispose();
            junboChart = null;
        }
        if (junboPieChart) {
            junboPieChart.dispose();
            junboPieChart = null;
        }
        if (junboAgeChart) {
            junboAgeChart.dispose();
            junboAgeChart = null;
        }
    }
})

// 监听艺术区折叠面板状态变化
watch(yishuquMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initYishuquChart();
            initYishuquPieChart();
            initYishuquAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (yishuquChart) {
            yishuquChart.dispose();
            yishuquChart = null;
        }
        if (yishuquPieChart) {
            yishuquPieChart.dispose();
            yishuquPieChart = null;
        }
        if (yishuquAgeChart) {
            yishuquAgeChart.dispose();
            yishuquAgeChart = null;
        }
    }
})

// 监听环球折叠面板状态变化
watch(huanqiuMianban, (newVal) => {
    if (newVal.includes('1')) {
        // 面板展开时，延迟初始化图表（确保动画完成）
        setTimeout(() => {
            initHuanqiuChart();
            initHuanqiuPieChart();
            initHuanqiuAgeChart();
        }, 400);
    } else {
        // 面板收起时，销毁图表实例
        if (huanqiuChart) {
            huanqiuChart.dispose();
            huanqiuChart = null;
        }
        if (huanqiuPieChart) {
            huanqiuPieChart.dispose();
            huanqiuPieChart = null;
        }
        if (huanqiuAgeChart) {
            huanqiuAgeChart.dispose();
            huanqiuAgeChart = null;
        }
    }
})








onMounted(() => {
    // 初始时如果面板是展开的，初始化图表
    if (gugongMianban.value.includes('1')) {
        setTimeout(() => {
            initGugongChart();
            initGugongPieChart();
            initGugongAgeChart();
        }, 500);
    }
    if (tiantanMianban.value.includes('1')) {
        setTimeout(() => {
            initTiantanChart();
            initTiantanPieChart();
            initTiantanAgeChart();
        }, 500);
    }
    if (yiheyuanMianban.value.includes('1')) {
        setTimeout(() => {
            initYiheyuanChart();
            initYiheyuanPieChart();
            initYiheyuanAgeChart();
        }, 500);
    }
    if (yuanmingyuanMianban.value.includes('1')) {
        setTimeout(() => {
            initYuanmingyuanChart();
            initYuanmingyuanPieChart();
            initYuanmingyuanAgeChart();
        }, 500);
    }
    if (changchengMianban.value.includes('1')) {
        setTimeout(() => {
            initChangchengChart();
            initChangchengPieChart();
            initChangchengAgeChart();
        }, 500);
    }
    if (beihaiMianban.value.includes('1')) {
        setTimeout(() => {
            initBeihaiChart();
            initBeihaiPieChart();
            initBeihaiAgeChart();
        }, 500);
    }
    if (yonghegongMianban.value.includes('1')) {
        setTimeout(() => {
            initYonghegongChart();
            initYonghegongPieChart();
            initYonghegongAgeChart();
        }, 500);
    }
    if (guoboMianban.value.includes('1')) {
        setTimeout(() => {
            initGuoboChart();
            initGuoboPieChart();
            initGuoboAgeChart();
        }, 500);
    }
    if (niaochaoMianban.value.includes('1')) {
        setTimeout(() => {
            initNiaochaoChart();
            initNiaochaoPieChart();
            initNiaochaoAgeChart();
        }, 500);
    }
    if (shuilifangMianban.value.includes('1')) {
        setTimeout(() => {
            initShuilifangChart();
            initShuilifangPieChart();
            initShuilifangAgeChart();
        }, 500);
    }
    if (xiangshanMianban.value.includes('1')) {
        setTimeout(() => {
            initXiangshanChart();
            initXiangshanPieChart();
            initXiangshanAgeChart();
        }, 500);
    }
    if (nanluoguxiangMianban.value.includes('1')) {
        setTimeout(() => {
            initNanluoguxiangChart();
            initNanluoguxiangPieChart();
            initNanluoguxiangAgeChart();
        }, 500);
    }
    if (shichahaiMianban.value.includes('1')) {
        setTimeout(() => {
            initShichahaiChart();
            initShichahaiPieChart();
            initShichahaiAgeChart();
        }, 500);
    }
    if (junboMianban.value.includes('1')) {
        setTimeout(() => {
            initJunboChart();
            initJunboPieChart();
            initJunboAgeChart();
        }, 500);
    }
    if (yishuquMianban.value.includes('1')) {
        setTimeout(() => {
            initYishuquChart();
            initYishuquPieChart();
            initYishuquAgeChart();
        }, 500);
    }
    if (huanqiuMianban.value.includes('1')) {
        setTimeout(() => {
            initHuanqiuChart();
            initHuanqiuPieChart();
            initHuanqiuAgeChart();
        }, 500);
    }
});

// 组件卸载时清理
import { onUnmounted } from 'vue';
onUnmounted(() => {
    if (gugongChart) {
        gugongChart.dispose();
        gugongChart = null;
    }
    if (tiantanChart) {
        tiantanChart.dispose();
        tiantanChart = null;
    }
    if (yiheyuanChart) {
        yiheyuanChart.dispose();
        yiheyuanChart = null;
    }
    if (yuanmingyuanChart) {
        yuanmingyuanChart.dispose();
        yuanmingyuanChart = null;
    }
    if (changchengChart) {
        changchengChart.dispose();
        changchengChart = null;
    }
    if (beihaiChart) {
        beihaiChart.dispose();
        beihaiChart = null;
    }
    if (yonghegongChart) {
        yonghegongChart.dispose();
        yonghegongChart = null;
    }
    if (guoboChart) {
        guoboChart.dispose();
        guoboChart = null;
    }
    if (niaochaoChart) {
        niaochaoChart.dispose();
        niaochaoChart = null;
    }
    if (shuilifangChart) {
        shuilifangChart.dispose();
        shuilifangChart = null;
    }
    if (xiangshanChart) {
        xiangshanChart.dispose();
        xiangshanChart = null;
    }
    if (nanluoguxiangChart) {
        nanluoguxiangChart.dispose();
        nanluoguxiangChart = null;
    }
    if (shichahaiChart) {
        shichahaiChart.dispose();
        shichahaiChart = null;
    }
    if (junboChart) {
        junboChart.dispose();
        junboChart = null;
    }
    if (yishuquChart) {
        yishuquChart.dispose();
        yishuquChart = null;
    }
    if (huanqiuChart) {
        huanqiuChart.dispose();
        huanqiuChart = null;
    }

    //===================
    if (gugongPieChart) {
        gugongPieChart.dispose();
        gugongPieChart = null;
    }
    if (tiantanPieChart) {
        tiantanPieChart.dispose();
        tiantanPieChart = null;
    }
    if (yiheyuanPieChart) {
        yiheyuanPieChart.dispose();
        yiheyuanPieChart = null;
    }
    if (yuanmingyuanPieChart) {
        yuanmingyuanPieChart.dispose();
        yuanmingyuanPieChart = null;
    }
    if (changchengPieChart) {
        changchengPieChart.dispose();
        changchengPieChart = null;
    }
    if (beihaiPieChart) {
        beihaiPieChart.dispose();
        beihaiPieChart = null;
    }
    if (yonghegongPieChart) {
        yonghegongPieChart.dispose();
        yonghegongPieChart = null;
    }
    if (guoboPieChart) {
        guoboPieChart.dispose();
        guoboPieChart = null;
    }
    if (niaochaoPieChart) {
        niaochaoPieChart.dispose();
        niaochaoPieChart = null;
    }
    if (shuilifangPieChart) {
        shuilifangPieChart.dispose();
        shuilifangPieChart = null;
    }
    if (xiangshanPieChart) {
        xiangshanPieChart.dispose();
        xiangshanPieChart = null;
    }
    if (nanluoguxiangPieChart) {
        nanluoguxiangPieChart.dispose();
        nanluoguxiangPieChart = null;
    }
    if (shichahaiPieChart) {
        shichahaiPieChart.dispose();
        shichahaiPieChart = null;
    }
    if (junboPieChart) {
        junboPieChart.dispose();
        junboPieChart = null;
    }
    if (yishuquPieChart) {
        yishuquPieChart.dispose();
        yishuquPieChart = null;
    }
    if (huanqiuPieChart) {
        huanqiuPieChart.dispose();
        huanqiuPieChart = null;
    }

    // ==================
    if (gugongAgeChart) {
        gugongAgeChart.dispose();
        gugongAgeChart = null;
    }
    if (tiantanAgeChart) {
        tiantanAgeChart.dispose();
        tiantanAgeChart = null;
    }
    if (yiheyuanAgeChart) {
        yiheyuanAgeChart.dispose();
        yiheyuanAgeChart = null;
    }
    if (yuanmingyuanAgeChart) {
        yuanmingyuanAgeChart.dispose();
        yuanmingyuanAgeChart = null;
    }
    if (changchengAgeChart) {
        changchengAgeChart.dispose();
        changchengAgeChart = null;
    }
    if (beihaiAgeChart) {
        beihaiAgeChart.dispose();
        beihaiAgeChart = null;
    }
    if (yonghegongAgeChart) {
        yonghegongAgeChart.dispose();
        yonghegongAgeChart = null;
    }
    if (guoboAgeChart) {
        guoboAgeChart.dispose();
        guoboAgeChart = null;
    }
    if (niaochaoAgeChart) {
        niaochaoAgeChart.dispose();
        niaochaoAgeChart = null;
    }
    if (shuilifangAgeChart) {
        shuilifangAgeChart.dispose();
        shuilifangAgeChart = null;
    }
    if (xiangshanAgeChart) {
        xiangshanAgeChart.dispose();
        xiangshanAgeChart = null;
    }
    if (nanluoguxiangAgeChart) {
        nanluoguxiangAgeChart.dispose();
        nanluoguxiangAgeChart = null;
    }
    if (shichahaiAgeChart) {
        shichahaiAgeChart.dispose();
        shichahaiAgeChart = null;
    }
    if (junboAgeChart) {
        junboAgeChart.dispose();
        junboAgeChart = null;
    }
    if (yishuquAgeChart) {
        yishuquAgeChart.dispose();
        yishuquAgeChart = null;
    }
    if (huanqiuAgeChart) {
        huanqiuAgeChart.dispose();
        huanqiuAgeChart = null;
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
    margin-bottom: 20px;
    background-color: #f2ece6;
}

.document-list {
    margin-bottom: 20px;
    background-color: #f2ece6;
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
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

/* 轮播图样式 */
.carousel-container {
    width: 100%;
    height: 500px;
    overflow: hidden;
    position: relative;
    box-sizing: border-box;
}

.el-carousel__item {
    height: 500px !important;
}

.carousel-item-bg {
    width: 100%;
    height: 500px;
    background-size: cover;
    background-position: center;
}

/* 折叠面板样式 */
.el-collapse {
    min-height: 100px;
}

::v-deep(.el-collapse-item__header) {
    min-height: 120px;
    height: auto !important;
    display: flex;
    align-items: center;
    padding: 20px;
    background-color: white;
    border-radius: 8px;
    margin-bottom: 10px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
}

::v-deep(.el-collapse-item__content) {
    padding: 30px;
    background-color: white;
    border-radius: 0 0 8px 8px;
    min-height: 500px;
}

/* 面板头部样式 */
.panel-header {
    display: flex;
    align-items: center;
    width: 100%;
}

.panel-image-container {
    width: 300px;
    height: 400px;
    margin-right: 20px;
    border-radius: 8px;
    overflow: hidden;
    flex-shrink: 0;
}

.panel-image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.panel-title {
    font-size: 20px;
    font-weight: bold;
    color: #333;
}

/* 面板内容样式 */
.panel-content {
    padding: 20px 0;
}

.panel-content h3 {
    color: #333;
    margin-bottom: 15px;
    font-size: 24px;
}

.panel-content p {
    color: #666;
    line-height: 2。0;
    margin-bottom: 10px;
    font-size: large;
}

/* 图表区域样式 */
.chart-section {
    margin: 30px 0;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 8px;
}

.chart-section h4 {
    color: #333;
    margin-bottom: 15px;
    text-align: center;
}

/* 新增：图表行样式 */
.chart-row {
    display: flex;
    gap: 20px;
    margin: 30px 0;
}

.chart-half {
    flex: 1;
    margin: 0;
}

.pictorial-bar-container {
    width: 100%;
    height: 400px;
    background-color: white;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
}

.pie-chart-container {
    width: 100%;
    height: 400px;
    background-color: white;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
}

.chart-footer {
    font-size: 12px;
    color: #999;
    text-align: center;
    margin-top: 10px;
    font-style: italic;
}

/* 景点信息样式 */
.attraction-info {
    margin-top: 30px;
}

.attraction-info h4 {
    color: #333;
    margin-bottom: 15px;
}

.attraction-info ul {
    list-style-type: none;
    padding: 0;
}

.attraction-info li {
    padding: 8px 0;
    color: #666;
    border-bottom: 1px solid #f0f0f0;
    font-size: large;
}

.attraction-info li:before {
    content: "•";
    color: #d37a90;
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .logo-text {
        font-size: 40px;
    }

    .panel-image-container {
        width: 60px;
        height: 60px;
        margin-right: 15px;
    }

    .panel-title {
        font-size: 18px;
    }

    ::v-deep(.el-collapse-item__header) {
        min-height: 100px;
        padding: 15px;
    }

    .pictorial-bar-container,
    .pie-chart-container {
        height: 300px;
    }

    .chart-section {
        padding: 15px;
    }

    /* 移动端调整图表行布局 */
    .chart-row {
        flex-direction: column;
        gap: 15px;
    }

    .chart-half {
        width: 100%;
    }
}

/* 图表容器布局优化 */
.chart-section+.chart-section {
    margin-top: 40px;
}

/* 饼图特定样式 */
.pie-chart-container {
    position: relative;
}

.bordered-table {
    width: 100%;
    /* 或者指定具体像素值，如 800px */
    max-width: 1000px;
    /* 设置最大宽度 */
    margin: 20px 0;
    /* 居中显示 */
    font-size: 14px;
    /* 调整表格整体字体大小 */
}

.bordered-table th,
.bordered-table td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
    font-size: 14px;
    /* 表格内容字体大小 */
}

.bordered-table th {
    background-color: #f5f5f5;
    font-weight: bold;
    font-size: 16px;
    /* 表头字体大小 */
}

.bordered-table tr:nth-child(even) {
    background-color: #f9f9f9;
}

.bordered-table tr:hover {
    background-color: #f0f0f0;
}
</style>