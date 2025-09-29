# douyin_logistics_app.py
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

st.set_page_config(page_title="侯良语 面试Demo", layout="wide")

# 添加全局CSS样式
st.markdown("""
<style>
    /* 全局样式 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* 标题样式 */
    h1 {
        color: #1976d2;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    h2 {
        color: #424242;
        border-bottom: 3px solid #2196f3;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    
    h3 {
        color: #616161;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* 侧边栏样式 */
    .css-1d391kg {
        background-color: #f5f5f5;
    }
    
    /* 数据表格样式 */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* 图表容器样式 */
    .stPlotlyChart {
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* 按钮样式 */
    .stButton > button {
        background-color: #2196f3;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1976d2;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* 指标卡片样式 */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* 成功提示样式 */
    .success-box {
        background-color: #e8f5e8;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    
    /* 信息提示样式 */
    .info-box {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎯 抖音电商 — 物流履约业务 Demo")

page = st.sidebar.radio("页面", ["说明", "对比与发展", "履约指标决策树", "平台/商家/用户可视化", "优质快递体验验证", "偏远地区物流验证", "Work in Progress"], index=0)
# st.sidebar.markdown(
#     """
#     <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; margin: 10px 0;">
#         <h4 style="color: #1976d2; margin: 0 0 10px 0;">📋 术语说明</h4>
#         <p style="margin: 5px 0; color: #424242;"><strong>平台</strong> = 抖音电商</p>
#         <p style="margin: 5px 0; color: #424242;"><strong>商家</strong> = 入驻抖音卖货的商家</p>
#         <p style="margin: 5px 0; color: #424242;"><strong>用户</strong> = 抖音购物用户</p>
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

# ---------------- Page 1: 说明 ----------------
if page == "说明":
    # st.header("说明")
    st.markdown(
        """
        <div style="background-color: #e8f5e8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #4caf50;">
            <h3 style="color: #2e7d32; margin: 0 0 15px 0;">🎯 目标</h3>
            <p style="color: #424242; margin: 10px 0; font-size: 16px;">
                该Demo旨在通过对以下五个维度的分析，展示候选人对业务和岗位内容的快速学习和理解能力：
            </p>
            <ol style="color: #424242; margin: 15px 0; padding-left: 20px;">
                <li style="margin: 8px 0;">📈 抖音物流的发展历程</li>
                <li style="margin: 8px 0;">🎯 抖音电商物流履约指标体系</li>
                <li style="margin: 8px 0;">📊 平台/商家/用户视角分析的可视化</li>
                <li style="margin: 8px 0;">🔬 优质快递体验验证 - AB测试与因果分析</li>
                <li style="margin: 8px 0;">🗺️ 偏远地区物流业务验证 - 因果推断与ROI分析</li>
            </ol>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # 开发日志
    st.markdown("""
    <div style="background-color: #f3e5f5; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #9c27b0;">
        <h3 style="color: #7b1fa2; margin: 0 0 15px 0;">📋 开发日志</h3>
        """, 
        unsafe_allow_html=True
    )
    
    with st.expander("点击展开查看开发历史", expanded=False):
        st.markdown("""
        **v3.0 (2025-09-27 更新)**
        - ✨ 新增优质快递体验验证模块
        - ✨ 新增偏远地区物流验证模块  
        - 🔬 强化因果推断能力展示
        - 📊 完善数据可视化功能
        
        **v1.0 (2025-09-25 初始版本)**
        - 基础物流履约指标体系
        - 平台/商家/用户多视角分析
        - 抖音电商物流发展历程回顾
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 红色警示文字
    st.markdown(
        """
        <div style="background-color: #ffebee; border-left: 4px solid #f44336; padding: 10px; margin: 10px 0; border-radius: 4px;">
            <p style="color: #d32f2f; font-weight: bold; margin: 0;">
                ⚠️ 注意：该Demo使用的数据均来自于互联网公开信息和模拟数据，仅作展示和学习使用。
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# ---------------- Page 2: 对比与发展 ----------------
elif page == "对比与发展":
    st.header("抖音电商物流模式发展回顾 & 横向对比")

    # 国内电商平台近十年市场份额对比
    st.subheader("📈 国内电商平台近十年市场份额对比")
    
    # 创建市场份额数据
    market_share_data = pd.DataFrame({
        'year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        '阿里': [76.2, 75.8, 73.5, 70.2, 66.8, 61.5, 55.8, 52.1, 48.9, 45.2, 42.1],
        '京东': [18.5, 19.2, 20.8, 22.1, 23.5, 24.8, 25.2, 24.9, 24.1, 23.5, 22.8],
        '拼多多': [0, 0, 0.1, 0.8, 3.2, 7.8, 12.5, 15.8, 18.2, 20.1, 21.5],
        '抖音电商': [0, 0, 0, 0, 0.1, 0.3, 1.2, 3.5, 5.8, 7.2, 8.9],
        '快手电商': [0, 0, 0, 0, 0, 0.1, 0.8, 1.5, 2.1, 2.8, 3.2],
        '小红书': [0, 0, 0, 0, 0, 0.1, 0.2, 0.5, 0.8, 1.1, 1.3],
        '其他': [5.3, 5.0, 5.6, 6.9, 6.4, 5.5, 4.3, 1.7, 0.1, 0.1, 0.2]
    })
    
    # 创建堆叠面积图
    market_share_long = market_share_data.melt(
        id_vars=['year'], 
        var_name='platform', 
        value_name='share'
    )
    
    # 设置颜色方案
    color_scale = alt.Scale(domain=['阿里', '京东', '拼多多', '抖音电商', '快手电商', '小红书', '其他'],
                           range=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#DDA0DD'])
    
    market_share_chart = alt.Chart(market_share_long).mark_area(
        interpolate='monotone',
        opacity=0.8
    ).encode(
        x=alt.X('year:O', title='年份', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('share:Q', title='市场份额 (%)', scale=alt.Scale(domain=[0, 100])),
        color=alt.Color('platform:N', scale=color_scale, title='平台'),
        tooltip=['year:O', 'platform:N', alt.Tooltip('share:Q', title='市场份额', format='.1f')]
    ).properties(
        height=400,
        title=alt.TitleParams(
            text='国内电商平台市场份额变化趋势 (2014-2024)',
            fontSize=16,
            fontWeight='bold',
            color='#2C3E50'
        )
    ).resolve_scale(color='independent')
    
    st.altair_chart(market_share_chart, use_container_width=True)
    
    # 添加关键洞察
    st.markdown("""
    <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">🔍 关键洞察</h4>
        <ul style="color: #424242; margin: 0; padding-left: 20px;">
            <li><strong>阿里系</strong>：从2014年的76.2%下降至2024年的42.1%，但仍保持领先地位</li>
            <li><strong>拼多多</strong>：2018年快速崛起，2024年市场份额达21.5%，成为第二大电商平台</li>
            <li><strong>抖音电商</strong>：2020年开始发力，2024年市场份额达8.9%，增长迅猛</li>
            <li><strong>快手电商</strong>：2020年起步，2024年市场份额3.2%，稳步增长</li>
            <li><strong>市场格局</strong>：从"双寡头"向"多强竞争"转变，新兴平台快速崛起</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 纵向发展回顾时间线 - 炫酷版本
    st.subheader("🚀 纵向发展回顾")
    
    # 创建更丰富的时间线数据
    timeline = pd.DataFrame({
        'date': pd.to_datetime(["2018-01-01","2020-06-01","2021-01-01","2021-05-01","2022-01-01","2022-05-01","2022-09-01","2024-01-01"]),
        'metric':[15,35,45,55,65,75,85,90],
        'label': [
            '抖音小店上线，轻资产模式全盘外包',
            '直播带货兴起，物流需求激增',
            '推出字节面单系统，切断外部面单',
            '成立物流科技公司，强化供应链',
            '推出音尊达服务，联合通达系',
            '发布云仓产品，智能分单系统',
            '抖音超市小时达/次日达服务',
            '下线音需达，测试我的快递功能'
        ],
        'phase': ['初期探索', '初期探索', '体系升级', '体系升级', '服务聚合', '服务聚合', '服务聚合', '战略调整'],
        'color': ['#FF6B6B', '#FF6B6B', '#4ECDC4', '#4ECDC4', '#45B7D1', '#45B7D1', '#45B7D1', '#96CEB4']
    })
    
    # 创建渐变背景区域
    background = alt.Chart(timeline).mark_area(
        interpolate='monotone',
        opacity=0.1
    ).encode(
        x='date:T',
        y='metric:Q',
        color=alt.value('#4ECDC4')
    )
    
    # 创建主线条
    line = alt.Chart(timeline).mark_line(
        strokeWidth=4,
        interpolate='monotone'
    ).encode(
        x='date:T',
        y='metric:Q',
        color=alt.value('#2E86AB')
    )
    
    # 创建数据点
    points = alt.Chart(timeline).mark_circle(
        size=100,
        stroke='white',
        strokeWidth=3
    ).encode(
        x='date:T',
        y='metric:Q',
        color=alt.Color('color:N', scale=None),
        tooltip=['date:T', 'label:N', 'phase:N']
    )
    
    # 创建标签
    labels = alt.Chart(timeline).mark_text(
        align='center',
        dy=-25,
        fontSize=11,
        fontWeight='bold',
        color='#2C3E50'
    ).encode(
        x='date:T',
        y='metric:Q',
        text='label:N'
    )
    
    # 创建阶段标签
    phase_labels = alt.Chart(timeline).mark_text(
        align='center',
        dy=25,
        fontSize=10,
        color='#7F8C8D'
    ).encode(
        x='date:T',
        y='metric:Q',
        text='phase:N'
    )
    
    # 组合所有元素
    timeline_chart = (background + line + points + labels + phase_labels).resolve_scale(
        color='independent'
    ).properties(
        height=400,
        title=alt.TitleParams(
            text="抖音电商物流发展历程",
            fontSize=16,
            fontWeight='bold',
            color='#2C3E50'
        )
    )
    
    st.altair_chart(timeline_chart, use_container_width=True)

    # 横向文字对比表
    st.subheader("📊 横向对比：抖音 vs 京东 / 阿里 / 拼多多 / 快手 / 小红书")
    
    # 美化对比表格
    comp_data = {
        "平台": ["抖音电商", "京东", "阿里(淘宝/天猫)", "拼多多", "快手电商", "小红书"],
        "物流模式摘要": [
            "轻资产模式+字节面单系统；音尊达/云仓/抖音超市等多元化尝试；2024年战略调整，下线部分服务。",
            "自营+京东物流为核心，仓储网点密集、时效稳定；适合时效敏感型品类。",
            "天猫/淘宝生态中商家+菜鸟/快递公司组合，平台提供运力协同与履约保障工具。",
            "轻资产模式，主要依赖第三方物流；通过拼团模式降低物流成本，注重性价比。",
            "内容+电商模式，物流主要依赖第三方；快手小店快速发展，物流体系正在完善。",
            "以内容社区导购为主，电商还在发展中，物流多依赖第三方商家与快递。"
        ],
        "对比要点": [
            "内容->交易，物流控制力逐步增强但仍有局限",
            "重资产物流，端到端掌控力强",
            "成熟的商家履约规则与赔付机制",
            "轻资产运营，成本控制优先，物流效率逐步提升",
            "内容驱动转化，履约模式正快速迭代",
            "内容驱动转化，履约模式正快速迭代"
        ]
    }
    
    comp = pd.DataFrame(comp_data)
    
    # 使用样式化的表格
    st.markdown("""
    <style>
    .comparison-table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-radius: 8px;
        overflow: hidden;
    }
    .comparison-table th {
        background-color: #2196f3;
        color: white;
        padding: 15px;
        text-align: left;
        font-weight: bold;
    }
    .comparison-table td {
        padding: 15px;
        border-bottom: 1px solid #e0e0e0;
        vertical-align: top;
    }
    .comparison-table tr:nth-child(even) {
        background-color: #f5f5f5;
    }
    .comparison-table tr:hover {
        background-color: #e3f2fd;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.dataframe(comp, use_container_width=True)

    # 横向对比图
    st.subheader("横向对比图：配送时效 vs 平台控制力")
    df_cmp = pd.DataFrame({
        'platform': ['抖音电商','京东','阿里','拼多多','快手电商','小红书'],
        '配送时效': [60,90,80,65,55,50],
        '平台控制力': [50,95,80,45,40,35]
    })
    chart_cmp = alt.Chart(df_cmp).transform_fold(
        ['配送时效','平台控制力'], as_=['指标','数值']
    ).mark_bar().encode(
        x=alt.X('platform:N', sort=None),
        y=alt.Y('数值:Q'),
        color=alt.Color('指标:N'),
        tooltip=['platform:N','指标:N','数值:Q']
    ).properties(height=300)
    st.altair_chart(chart_cmp, use_container_width=True)
    
    # 添加更详细的对比分析
    st.subheader("📊 综合对比分析")
    
    # 创建雷达图数据
    comparison_radar = pd.DataFrame({
        '平台': ['抖音电商', '京东', '阿里', '拼多多', '快手电商', '小红书'],
        '配送时效': [60, 90, 80, 65, 55, 50],
        '平台控制力': [50, 95, 80, 45, 40, 35],
        '成本控制': [70, 60, 75, 90, 65, 60],
        '用户体验': [75, 85, 80, 70, 65, 60],
        '技术投入': [80, 90, 85, 60, 50, 45]
    })
    
    # 创建多维度对比图
    col1, col2 = st.columns(2)
    
    with col1:
        # 配送时效对比
        delivery_chart = alt.Chart(comparison_radar).mark_bar(
            cornerRadius=5
        ).encode(
            x=alt.X('平台:N', sort=None),
            y=alt.Y('配送时效:Q', title='配送时效评分'),
            color=alt.Color('平台:N', scale=alt.Scale(scheme='category20')),
            tooltip=['平台:N', '配送时效:Q']
        ).properties(
            height=300,
            title='🚚 配送时效对比'
        )
        st.altair_chart(delivery_chart, use_container_width=True)
        
        # 平台控制力对比
        control_chart = alt.Chart(comparison_radar).mark_bar(
            cornerRadius=5
        ).encode(
            x=alt.X('平台:N', sort=None),
            y=alt.Y('平台控制力:Q', title='平台控制力评分'),
            color=alt.Color('平台:N', scale=alt.Scale(scheme='category20')),
            tooltip=['平台:N', '平台控制力:Q']
        ).properties(
            height=300,
            title='🎯 平台控制力对比'
        )
        st.altair_chart(control_chart, use_container_width=True)
    
    with col2:
        # 成本控制对比
        cost_chart = alt.Chart(comparison_radar).mark_bar(
            cornerRadius=5
        ).encode(
            x=alt.X('平台:N', sort=None),
            y=alt.Y('成本控制:Q', title='成本控制评分'),
            color=alt.Color('平台:N', scale=alt.Scale(scheme='category20')),
            tooltip=['平台:N', '成本控制:Q']
        ).properties(
            height=300,
            title='💰 成本控制对比'
        )
        st.altair_chart(cost_chart, use_container_width=True)
        
        # 用户体验对比
        ux_chart = alt.Chart(comparison_radar).mark_bar(
            cornerRadius=5
        ).encode(
            x=alt.X('平台:N', sort=None),
            y=alt.Y('用户体验:Q', title='用户体验评分'),
            color=alt.Color('平台:N', scale=alt.Scale(scheme='category20')),
            tooltip=['平台:N', '用户体验:Q']
        ).properties(
            height=300,
            title='😊 用户体验对比'
        )
        st.altair_chart(ux_chart, use_container_width=True)

   
# ---------------- Page 3: 履约指标决策树 ----------------
elif page == "履约指标决策树":
    st.header("🎯 适配抖音电商的物流履约指标决策树")
    
    # 指标层级说明
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 10px; border-radius: 4px; margin: 5px 0;">
                <h4 style="color: #1976d2; margin: 0;">🔵 一级指标</h4>
                <p style="color: #424242; margin: 5px 0 0 0; font-size: 14px;">核心业务指标</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 10px; border-radius: 4px; margin: 5px 0;">
                <h4 style="color: #7b1fa2; margin: 0;">🟣 二级指标</h4>
                <p style="color: #424242; margin: 5px 0 0 0; font-size: 14px;">细分业务指标</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 10px; border-radius: 4px; margin: 5px 0;">
                <h4 style="color: #388e3c; margin: 0;">🟢 三级指标</h4>
                <p style="color: #424242; margin: 5px 0 0 0; font-size: 14px;">具体执行指标</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # 美化版决策树
    decision_tree_dot = r"""
    digraph G {
      rankdir=TB;
      node [fontname="Microsoft YaHei", fontsize=12];
      
      // 一级指标 - 蓝色
      履约绩效 [shape=box, style=filled, fillcolor="#e3f2fd", color="#1976d2", fontcolor="#1976d2", fontsize=14, fontweight=bold];
      
      // 二级指标 - 紫色
      交付时效 [shape=box, style=filled, fillcolor="#f3e5f5", color="#7b1fa2", fontcolor="#7b1fa2"];
      交付完整性 [shape=box, style=filled, fillcolor="#f3e5f5", color="#7b1fa2", fontcolor="#7b1fa2"];
      异常率 [shape=box, style=filled, fillcolor="#f3e5f5", color="#7b1fa2", fontcolor="#7b1fa2"];
      
      // 三级指标 - 绿色
      下单到发货时间 [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
      发货到收货时间 [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
      缺货率 [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
      换退货率 [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
      破损率 [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
      送达误差率 [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
      
      // 四级指标 - 浅绿色
      平均下单到发货小时数 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      超48h未发货率 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      平均物流时长天 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      次日达隔日达占比 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      在途缺货报警次数 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      因物流导致退货占比 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      包裹破损件数每万单 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      错投率 [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38"];
      
      // 连接关系
      履约绩效 -> 交付时效;
      履约绩效 -> 交付完整性;
      履约绩效 -> 异常率;
      交付时效 -> 下单到发货时间;
      交付时效 -> 发货到收货时间;
      下单到发货时间 -> 平均下单到发货小时数;
      下单到发货时间 -> 超48h未发货率;
      发货到收货时间 -> 平均物流时长天;
      发货到收货时间 -> 次日达隔日达占比;
      交付完整性 -> 缺货率;
      交付完整性 -> 换退货率;
      缺货率 -> 在途缺货报警次数;
      换退货率 -> 因物流导致退货占比;
      异常率 -> 破损率;
      异常率 -> 送达误差率;
      破损率 -> 包裹破损件数每万单;
      送达误差率 -> 错投率;
    }
    """
    st.graphviz_chart(decision_tree_dot)

# ---------------- Page 4: 平台/商家/用户 可视化 ----------------
elif page == "平台/商家/用户可视化":
    st.header("📊 平台 / 商家 / 用户：核心指标模拟可视化")
    
    # 设置配色方案
    colors = {
        'primary': '#2E86AB',
        'secondary': '#A23B72', 
        'success': '#F18F01',
        'warning': '#C73E1D',
        'info': '#4ECDC4',
        'light': '#F7F7F7'
    }

    rng = np.random.default_rng(42)
    dates = pd.date_range(end=datetime.today(), periods=30)
    platform_df = pd.DataFrame({
        'date': dates,
        'orders': rng.integers(8000,12000,30),
        'on_time_rate': (rng.random(30)*0.1 + 0.85).round(3),
        'damage_rate': (rng.random(30)*0.01 + 0.005).round(4),
        'return_rate': (rng.random(30)*0.02 + 0.01).round(3)
    })
    merchant_df = pd.DataFrame({
        'merchant':[f'商家{i}' for i in range(1,6)],
        'avg_ship_hours':[12,48,24,8,36],
        'next_day_ratio':[0.6,0.2,0.45,0.75,0.3],
        'return_rate':[0.02,0.05,0.03,0.01,0.04],
        'damage_rate':[0.005,0.01,0.007,0.003,0.008]
    })
    user_df = pd.DataFrame({
        'user_type':['高价值用户','普通用户','新用户','海外用户'],
        'expect_days':[1,2,3,5],
        'satisfaction':[0.85,0.75,0.65,0.6],
        'avg_wait_days':[1.2,2.1,3.0,4.5],
        'return_rate':[0.01,0.03,0.05,0.08]
    })

    # 平台视角 - 美化版本
    st.subheader('🏢 平台视角')
    col1, col2 = st.columns(2)
    
    with col1:
        # 订单量趋势图
        orders_chart = alt.Chart(platform_df).mark_area(
            interpolate='monotone',
            color=colors['primary'],
            opacity=0.7
        ).add_selection(
            alt.selection_interval(bind='scales')
        ).encode(
            x=alt.X('date:T', title='日期', axis=alt.Axis(format='%m-%d')),
            y=alt.Y('orders:Q', title='订单量', scale=alt.Scale(zero=False)),
            tooltip=['date:T', alt.Tooltip('orders:Q', title='订单量', format='.0f')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='📈 日订单量趋势',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(orders_chart, use_container_width=True)
        
        # 准时率趋势图
        ontime_chart = alt.Chart(platform_df).mark_line(
            strokeWidth=3,
            color=colors['success']
        ).encode(
            x=alt.X('date:T', title='日期', axis=alt.Axis(format='%m-%d')),
            y=alt.Y('on_time_rate:Q', title='准时率', scale=alt.Scale(domain=[0.8, 1.0])),
            tooltip=['date:T', alt.Tooltip('on_time_rate:Q', title='准时率', format='.1%')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='⏰ 准时配送率',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(ontime_chart, use_container_width=True)
    
    with col2:
        # 破损率趋势图
        damage_chart = alt.Chart(platform_df).mark_line(
            strokeWidth=3,
            color=colors['warning']
        ).encode(
            x=alt.X('date:T', title='日期', axis=alt.Axis(format='%m-%d')),
            y=alt.Y('damage_rate:Q', title='破损率', scale=alt.Scale(zero=False)),
            tooltip=['date:T', alt.Tooltip('damage_rate:Q', title='破损率', format='.2%')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='📦 包裹破损率',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(damage_chart, use_container_width=True)
        
        # 退货率趋势图
        return_chart = alt.Chart(platform_df).mark_line(
            strokeWidth=3,
            color=colors['secondary']
        ).encode(
            x=alt.X('date:T', title='日期', axis=alt.Axis(format='%m-%d')),
            y=alt.Y('return_rate:Q', title='退货率', scale=alt.Scale(zero=False)),
            tooltip=['date:T', alt.Tooltip('return_rate:Q', title='退货率', format='.1%')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='🔄 退货率趋势',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(return_chart, use_container_width=True)

    # 商家视角 - 美化版本
    st.subheader('🏪 商家视角')
    
    # 商家数据表格 - 美化
    st.markdown("**商家履约表现对比**")
    styled_merchant_df = merchant_df.copy()
    styled_merchant_df['avg_ship_hours'] = styled_merchant_df['avg_ship_hours'].apply(lambda x: f"{x}小时")
    styled_merchant_df['next_day_ratio'] = styled_merchant_df['next_day_ratio'].apply(lambda x: f"{x:.1%}")
    styled_merchant_df['return_rate'] = styled_merchant_df['return_rate'].apply(lambda x: f"{x:.1%}")
    styled_merchant_df['damage_rate'] = styled_merchant_df['damage_rate'].apply(lambda x: f"{x:.1%}")
    st.dataframe(styled_merchant_df, use_container_width=True)
    
    # 商家图表
    col1, col2 = st.columns(2)
    
    with col1:
        # 平均发货时长
        ship_chart = alt.Chart(merchant_df).mark_bar(
            color=colors['info']
        ).encode(
            x='merchant:N',
            y='avg_ship_hours:Q',
            tooltip=['merchant:N', 'avg_ship_hours:Q']
        ).properties(
            height=300,
            title='⏱️ 平均发货时长对比'
        )
        st.altair_chart(ship_chart, use_container_width=True)
        
        # 次日达比例
        nextday_chart = alt.Chart(merchant_df).mark_bar(
            cornerRadius=8,
            color=colors['success']
        ).encode(
            x=alt.X('merchant:N', title='商家', sort=None),
            y=alt.Y('next_day_ratio:Q', title='次日达比例', scale=alt.Scale(domain=[0, 1])),
            tooltip=['merchant:N', alt.Tooltip('next_day_ratio:Q', title='次日达比例', format='.1%')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='🚀 次日达比例对比',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(nextday_chart, use_container_width=True)
    
    with col2:
        # 退货率对比
        return_merchant_chart = alt.Chart(merchant_df).mark_bar(
            cornerRadius=8,
            color=colors['warning']
        ).encode(
            x=alt.X('merchant:N', title='商家', sort=None),
            y=alt.Y('return_rate:Q', title='退货率'),
            tooltip=['merchant:N', alt.Tooltip('return_rate:Q', title='退货率', format='.1%')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='🔄 商家退货率对比',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(return_merchant_chart, use_container_width=True)
        
        # 破损率对比
        damage_merchant_chart = alt.Chart(merchant_df).mark_bar(
            cornerRadius=8,
            color=colors['secondary']
        ).encode(
            x=alt.X('merchant:N', title='商家', sort=None),
            y=alt.Y('damage_rate:Q', title='破损率'),
            tooltip=['merchant:N', alt.Tooltip('damage_rate:Q', title='破损率', format='.1%')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='📦 商家破损率对比',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(damage_merchant_chart, use_container_width=True)

    # 用户视角 - 美化版本
    st.subheader('👥 用户视角')
    
    # 用户数据表格 - 美化
    st.markdown("**用户类型履约体验对比**")
    styled_user_df = user_df.copy()
    styled_user_df['expect_days'] = styled_user_df['expect_days'].apply(lambda x: f"{x}天")
    styled_user_df['satisfaction'] = styled_user_df['satisfaction'].apply(lambda x: f"{x:.1%}")
    styled_user_df['avg_wait_days'] = styled_user_df['avg_wait_days'].apply(lambda x: f"{x:.1f}天")
    styled_user_df['return_rate'] = styled_user_df['return_rate'].apply(lambda x: f"{x:.1%}")
    st.dataframe(styled_user_df, use_container_width=True)
    
    # 用户图表
    col1, col2 = st.columns(2)
    
    with col1:
        # 用户满意度
        satisfaction_chart = alt.Chart(user_df).mark_bar(
            cornerRadius=8,
            color=colors['success']
        ).encode(
            x=alt.X('user_type:N', title='用户类型', sort=None),
            y=alt.Y('satisfaction:Q', title='满意度', scale=alt.Scale(domain=[0, 1])),
            tooltip=['user_type:N', alt.Tooltip('satisfaction:Q', title='满意度', format='.1%')]
        ).properties(
            height=300,
            title=alt.TitleParams(
                text='😊 用户满意度对比',
                fontSize=14,
                fontWeight='bold',
                color='#2C3E50'
            )
        )
        st.altair_chart(satisfaction_chart, use_container_width=True)
        
        # 平均等待天数
        wait_chart = alt.Chart(user_df).mark_bar(
            color=colors['info']
        ).encode(
            x='user_type:N',
            y='avg_wait_days:Q',
            tooltip=['user_type:N', 'avg_wait_days:Q']
        ).properties(
            height=300,
            title='⏳ 平均等待天数对比'
        )
        st.altair_chart(wait_chart, use_container_width=True)
    
    with col2:
        # 用户退货率
        user_return_chart = alt.Chart(user_df).mark_bar(
            color=colors['warning']
        ).encode(
            x='user_type:N',
            y='return_rate:Q',
            tooltip=['user_type:N', 'return_rate:Q']
        ).properties(
            height=300,
            title='🔄 用户退货率对比'
        )
        st.altair_chart(user_return_chart, use_container_width=True)
        
        # 期望vs实际配送天数对比
        expect_data = []
        for _, row in user_df.iterrows():
            expect_data.append({
                'user_type': row['user_type'],
                'days': row['expect_days'],
                'type': '期望天数'
            })
            expect_data.append({
                'user_type': row['user_type'],
                'days': row['avg_wait_days'],
                'type': '实际天数'
            })
        
        expect_vs_actual = pd.DataFrame(expect_data)
        
        expect_chart = alt.Chart(expect_vs_actual).mark_bar().encode(
            x='user_type:N',
            y='days:Q',
            color='type:N',
            tooltip=['user_type:N', 'type:N', 'days:Q']
        ).properties(
            height=300,
            title='📊 期望vs实际配送天数'
        )
        st.altair_chart(expect_chart, use_container_width=True)

# ---------------- Page 5: 优质快递体验验证 ---------------- 
elif page == "优质快递体验验证":
    st.header("🚀 优质快递体验验证 - AB测试与因果分析")
    
    # 实验设计说明
    st.subheader("🎯 实验设计")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">🔬 AB测试设计</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>实验组</strong>：优质快递（顺丰、京东物流）</li>
                <li><strong>对照组</strong>：普通快递（通达系）</li>
                <li><strong>样本量</strong>：每组10万订单</li>
                <li><strong>实验周期</strong>：30天</li>
                <li><strong>随机化</strong>：按用户ID哈希分组</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">📊 核心指标</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>主要指标</strong>：用户满意度、复购率</li>
                <li><strong>次要指标</strong>：NPS、配送时效、破损率</li>
                <li><strong>业务指标</strong>：GMV、客单价、LTV</li>
                <li><strong>成本指标</strong>：物流成本、客服成本</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 样本量计算与功效分析
    st.subheader("📊 样本量计算与功效分析")
    
    st.markdown("""
    <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #2e7d32; margin: 0 0 10px 0;">🧮 功效分析计算</h4>
        <p style="color: #424242; margin: 0;">
            <strong>基于历史数据</strong>：普通快递用户满意度75%、复购率40%、平均配送时长2.8天
        </p>
        <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
            <li><strong>α=0.05</strong>：假阳性率（5%显著性水平）</li>
            <li><strong>1-β=0.8</strong>：80%检测效力</li>
            <li><strong>MDE</strong>：满意度提升5%、复购率提升8%、配送时长缩短0.5天</li>
            <li><strong>最终确定</strong>：每组覆盖1000用户（合计2000）</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 实验设计详情
    st.markdown("### 📋 实验设计详情")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">🎯 实验组策略</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>快递服务</strong>：顺丰、京东物流</li>
                <li><strong>配送时效</strong>：当日达/次日达</li>
                <li><strong>包装标准</strong>：防震包装、易碎标识</li>
                <li><strong>客服支持</strong>：专属客服、实时跟踪</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">📊 对照组策略</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>快递服务</strong>：中通、圆通、韵达</li>
                <li><strong>配送时效</strong>：2-3天送达</li>
                <li><strong>包装标准</strong>：标准包装</li>
                <li><strong>客服支持</strong>：普通客服</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 随机分组方法
    st.markdown("### 🎲 随机分组方法")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">🎲 随机分组方法</h4>
        <ul style="color: #424242; margin: 0; padding-left: 20px;">
            <li><strong>分层随机</strong>：按城市等级、消费水平分层，确保每组在各维度分布相似</li>
            <li><strong>哈希算法</strong>：user_id % 2 确保同一用户始终在同一组，避免分组漂移</li>
            <li><strong>样本量</strong>：每组1000用户（合计2000）</li>
            <li><strong>时间窗口</strong>：30天实验周期</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 分组平衡性检验
    st.markdown("### ⚖️ 分组平衡性检验")
    
    balance_data = pd.DataFrame({
        '特征': ['平均年龄', '平均收入(元)', '城市等级', '历史购买频次', '商品类别偏好'],
        '实验组': [28.5, 8500, '一线:45%', 3.2, '数码:30%'],
        '对照组': [28.3, 8400, '一线:44%', 3.1, '数码:29%'],
        '差异': [0.2, 100, '1%', 0.1, '1%'],
        'p值': [0.85, 0.72, 0.68, 0.91, 0.76],
        '结论': ['平衡', '平衡', '平衡', '平衡', '平衡']
    })
    
    st.dataframe(balance_data, use_container_width=True)
    
    # 模拟AB测试数据
    st.subheader("📈 AB测试结果分析")
    
    # 生成模拟数据
    np.random.seed(42)
    n_samples = 1000
    
    # 实验组数据（优质快递）
    premium_data = {
        'delivery_time': np.random.normal(1.5, 0.5, n_samples),  # 1.5天平均
        'satisfaction': np.random.beta(8, 2, n_samples),  # 高满意度
        'repurchase_rate': np.random.beta(6, 4, n_samples),  # 较高复购率
        'damage_rate': np.random.beta(1, 99, n_samples),  # 低破损率
        'nps': np.random.normal(65, 15, n_samples),  # 高NPS
        'group': '优质快递'
    }
    
    # 对照组数据（普通快递）
    standard_data = {
        'delivery_time': np.random.normal(2.8, 0.8, n_samples),  # 2.8天平均
        'satisfaction': np.random.beta(6, 4, n_samples),  # 中等满意度
        'repurchase_rate': np.random.beta(4, 6, n_samples),  # 较低复购率
        'damage_rate': np.random.beta(3, 97, n_samples),  # 较高破损率
        'nps': np.random.normal(45, 20, n_samples),  # 中等NPS
        'group': '普通快递'
    }
    
    # 合并数据
    ab_data = pd.DataFrame({
        'delivery_time': np.concatenate([premium_data['delivery_time'], standard_data['delivery_time']]),
        'satisfaction': np.concatenate([premium_data['satisfaction'], standard_data['satisfaction']]),
        'repurchase_rate': np.concatenate([premium_data['repurchase_rate'], standard_data['repurchase_rate']]),
        'damage_rate': np.concatenate([premium_data['damage_rate'], standard_data['damage_rate']]),
        'nps': np.concatenate([premium_data['nps'], standard_data['nps']]),
        'group': ['优质快递'] * n_samples + ['普通快递'] * n_samples
    })
    
    # 关键指标对比
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        premium_satisfaction = ab_data[ab_data['group'] == '优质快递']['satisfaction'].mean()
        standard_satisfaction = ab_data[ab_data['group'] == '普通快递']['satisfaction'].mean()
        st.metric(
            "用户满意度", 
            f"{premium_satisfaction:.1%}", 
            f"{(premium_satisfaction - standard_satisfaction):.1%}"
        )
    
    with col2:
        premium_repurchase = ab_data[ab_data['group'] == '优质快递']['repurchase_rate'].mean()
        standard_repurchase = ab_data[ab_data['group'] == '普通快递']['repurchase_rate'].mean()
        st.metric(
            "复购率", 
            f"{premium_repurchase:.1%}", 
            f"{(premium_repurchase - standard_repurchase):.1%}"
        )
    
    with col3:
        premium_delivery = ab_data[ab_data['group'] == '优质快递']['delivery_time'].mean()
        standard_delivery = ab_data[ab_data['group'] == '普通快递']['delivery_time'].mean()
        st.metric(
            "平均配送时长", 
            f"{premium_delivery:.1f}天", 
            f"{(premium_delivery - standard_delivery):.1f}天"
        )
    
    with col4:
        premium_nps = ab_data[ab_data['group'] == '优质快递']['nps'].mean()
        standard_nps = ab_data[ab_data['group'] == '普通快递']['nps'].mean()
        st.metric(
            "NPS", 
            f"{premium_nps:.0f}", 
            f"{(premium_nps - standard_nps):.0f}"
        )
    
    # 可视化分析
    st.subheader("📊 实验结果可视化")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 满意度分布对比
        satisfaction_chart = alt.Chart(ab_data).mark_boxplot().encode(
            x='group:N',
            y='satisfaction:Q',
            color='group:N',
            tooltip=['group:N', 'satisfaction:Q']
        ).properties(
            height=300,
            title='用户满意度分布对比'
        )
        st.altair_chart(satisfaction_chart, use_container_width=True)
        
        # 配送时长分布对比
        delivery_chart = alt.Chart(ab_data).mark_boxplot().encode(
            x='group:N',
            y='delivery_time:Q',
            color='group:N',
            tooltip=['group:N', 'delivery_time:Q']
        ).properties(
            height=300,
            title='配送时长分布对比'
        )
        st.altair_chart(delivery_chart, use_container_width=True)
    
    with col2:
        # 复购率分布对比
        repurchase_chart = alt.Chart(ab_data).mark_boxplot().encode(
            x='group:N',
            y='repurchase_rate:Q',
            color='group:N',
            tooltip=['group:N', 'repurchase_rate:Q']
        ).properties(
            height=300,
            title='复购率分布对比'
        )
        st.altair_chart(repurchase_chart, use_container_width=True)
        
        # NPS分布对比
        nps_chart = alt.Chart(ab_data).mark_boxplot().encode(
            x='group:N',
            y='nps:Q',
            color='group:N',
            tooltip=['group:N', 'nps:Q']
        ).properties(
            height=300,
            title='NPS分布对比'
        )
        st.altair_chart(nps_chart, use_container_width=True)
    
    # 统计显著性检验详解
    st.subheader("🔬 统计显著性检验详解")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 满意度检验 (t-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用t-test？</strong>满意度是连续变量（0-1评分），t-test适用于连续数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                t = (x̄₁ - x̄₂) / s_p√(1/n₁ + 1/n₂)
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组满意度：0.80 ± 0.12</li>
                <li>对照组满意度：0.60 ± 0.15</li>
                <li>t统计量：12.5</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">📈 复购率检验 (Z-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用Z-test？</strong>复购率是二分类变量（复购/不复购），Z-test适用于比例数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                Z = (p₁ - p₂) / √(p(1-p)(1/n₁ + 1/n₂))
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组复购率：60%</li>
                <li>对照组复购率：40%</li>
                <li>Z统计量：8.2</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">⏱️ 配送时长检验 (t-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用t-test？</strong>配送时长是连续变量（天数），t-test适用于连续数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                t = (x̄₁ - x̄₂) / s_p√(1/n₁ + 1/n₂)
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组配送时长：1.5 ± 0.5天</li>
                <li>对照组配送时长：2.8 ± 0.8天</li>
                <li>t统计量：-15.2</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 统计检验结果汇总
    st.markdown("### 📋 统计检验结果汇总")
    
    test_results = pd.DataFrame({
        '指标': ['用户满意度', '复购率', '配送时长', 'NPS'],
        '实验组': ['80%', '60%', '1.5天', '65'],
        '对照组': ['60%', '40%', '2.8天', '45'],
        '提升幅度': ['+20%', '+20%', '-1.3天', '+20'],
        'p值': ['<0.001', '<0.001', '<0.001', '<0.001'],
        '显著性': ['***', '***', '***', '***']
    })
    
    st.dataframe(test_results, use_container_width=True)
    
    # 结果解读与业务落地
    st.subheader("🎯 结果解读与业务落地")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 统计显著性</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>所有核心指标p<0.001</li>
                <li>远小于α=0.05</li>
                <li>拒绝零假设</li>
                <li>结果可信度高</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">💼 业务显著性</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>满意度：60%→80%（+20%）</li>
                <li>复购率：40%→60%（+20%）</li>
                <li>配送时长：2.8→1.5天（-46%）</li>
                <li>均远超MDE阈值</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #7b1fa2; margin: 0 0 10px 0;">🧠 业务解释力</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>优质快递提升用户体验</li>
                <li>快速配送增强用户粘性</li>
                <li>专业包装降低破损率</li>
                <li>服务升级带来复购增长</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 因果分析
    st.subheader("🎯 因果推断分析")
    
    st.markdown("""
    <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #f57c00; margin: 0 0 10px 0;">🔍 双重差分法(DID)分析</h4>
        <p style="color: #424242; margin: 0;">
            通过控制时间趋势和选择偏差，验证优质快递对用户体验的因果效应。
            结果显示优质快递显著提升用户满意度15.2%，复购率提升8.7%。
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 成本效益分析
    st.subheader("💰 成本效益分析")
    
    cost_benefit_data = pd.DataFrame({
        '指标': ['物流成本增加', '用户满意度提升', '复购率提升', 'NPS提升', 'GMV增长', 'ROI'],
        '优质快递': ['+2.5元/单', '+15.2%', '+8.7%', '+20分', '+12.3%', '2.8x'],
        '普通快递': ['基准', '基准', '基准', '基准', '基准', '1.0x']
    })
    
    st.dataframe(cost_benefit_data, use_container_width=True)
    
    # 结论与建议
    st.subheader("📋 结论与建议")
    
    st.markdown("""
    <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #2e7d32; margin: 0 0 10px 0;">✅ 实验结论</h4>
        <ul style="color: #424242; margin: 0; padding-left: 20px;">
            <li>优质快递显著提升用户满意度和复购率</li>
            <li>虽然物流成本增加2.5元/单，但ROI达到2.8倍</li>
            <li>建议对高价值用户和重要商品使用优质快递</li>
            <li>可考虑分层服务策略，差异化物流体验</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------- Page 6: 偏远地区物流验证 ---------------- 
elif page == "偏远地区物流验证":
    st.header("🗺️ 偏远地区物流业务验证 - 因果推断与ROI分析")
    
    # 问题背景
    st.subheader("🎯 业务背景")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">📋 核心问题</h4>
        <p style="color: #424242; margin: 0;">
            抖音电商是否应该投入资源开展新疆、西藏等偏远地区的物流业务？
            如何通过数据驱动的方式验证这一决策的合理性？
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 样本量计算与功效分析
    st.subheader("📊 样本量计算与功效分析")
    
    st.markdown("""
    <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #2e7d32; margin: 0 0 10px 0;">🧮 功效分析计算</h4>
        <p style="color: #424242; margin: 0;">
            <strong>基于历史数据</strong>：偏远地区月订单量1.2万单、用户满意度72%、平均配送时长5.2天
        </p>
        <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
            <li><strong>α=0.05</strong>：假阳性率（5%显著性水平）</li>
            <li><strong>1-β=0.8</strong>：80%检测效力</li>
            <li><strong>MDE</strong>：订单量提升15%、满意度提升5%、配送时长缩短1天</li>
            <li><strong>最终确定</strong>：覆盖10个偏远地区，每个地区1000用户样本</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 实验设计详情
    st.markdown("### 📋 实验设计详情")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">🎯 实验组策略</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>物流网络</strong>：建立区域配送中心</li>
                <li><strong>配送时效</strong>：3-5天送达</li>
                <li><strong>服务标准</strong>：专业包装、实时跟踪</li>
                <li><strong>成本控制</strong>：批量配送、路线优化</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">📊 对照组策略</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>物流网络</strong>：依赖第三方物流</li>
                <li><strong>配送时效</strong>：5-7天送达</li>
                <li><strong>服务标准</strong>：标准包装</li>
                <li><strong>成本控制</strong>：单件配送</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 随机分组方法
    st.markdown("### 🎲 随机分组方法")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">🎲 随机分组方法</h4>
        <ul style="color: #424242; margin: 0; padding-left: 20px;">
            <li><strong>分层随机</strong>：按地区经济水平、人口规模分层，确保每组在各维度分布相似</li>
            <li><strong>哈希算法</strong>：region_id % 2 确保同一地区始终在同一组，避免分组漂移</li>
            <li><strong>样本量</strong>：每组5个地区，每地区1000用户（合计1万用户）</li>
            <li><strong>时间窗口</strong>：90天实验周期</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 分组平衡性检验
    st.markdown("### ⚖️ 分组平衡性检验")
    
    balance_data = pd.DataFrame({
        '特征': ['平均人口(万人)', '人均GDP(万元)', '历史订单量(万单)', '基础设施指数', '竞争激烈程度'],
        '实验组': [3200, 5.2, 1.8, 0.65, '中等'],
        '对照组': [3150, 5.1, 1.7, 0.63, '中等'],
        '差异': [50, 0.1, 0.1, 0.02, '无差异'],
        'p值': [0.85, 0.72, 0.68, 0.91, 'N/A'],
        '结论': ['平衡', '平衡', '平衡', '平衡', '平衡']
    })
    
    st.dataframe(balance_data, use_container_width=True)
    
    # 研究方法
    st.subheader("🔬 研究方法设计")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #7b1fa2; margin: 0 0 10px 0;">🎯 准实验设计</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>断点回归</strong>：分析偏远地区边界效应</li>
                <li><strong>工具变量</strong>：地理距离作为工具变量</li>
                <li><strong>双重差分</strong>：政策变化前后对比</li>
                <li><strong>匹配分析</strong>：PSM控制选择偏差</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 分析维度</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>需求分析</strong>：订单量、用户规模</li>
                <li><strong>成本分析</strong>：物流成本、基础设施</li>
                <li><strong>收益分析</strong>：GMV、用户LTV</li>
                <li><strong>竞争分析</strong>：市场份额、用户获取</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 模拟数据生成
    st.subheader("📈 偏远地区数据分析")
    
    # 生成模拟的偏远地区数据
    np.random.seed(42)
    
    # 地区分类数据
    regions_data = pd.DataFrame({
        'region': ['新疆', '西藏', '青海', '内蒙古', '甘肃', '宁夏', '云南', '贵州', '广西', '海南'],
        'population': [2585, 364, 592, 2405, 2502, 720, 4721, 3856, 5013, 1020],  # 万人
        'gdp_per_capita': [5.2, 4.8, 5.8, 7.2, 4.1, 5.5, 5.1, 4.9, 4.7, 6.5],  # 万元
        'logistics_cost': [8.5, 12.3, 7.8, 6.2, 7.1, 6.8, 5.9, 6.5, 5.7, 6.1],  # 元/单
        'delivery_time': [5.2, 7.8, 4.5, 3.8, 4.2, 3.9, 3.5, 3.8, 3.2, 3.6],  # 天
        'order_volume': [12000, 2800, 8500, 18000, 15000, 4200, 35000, 28000, 45000, 15000],  # 月订单量
        'user_satisfaction': [0.72, 0.68, 0.75, 0.78, 0.73, 0.76, 0.81, 0.79, 0.82, 0.80]
    })
    
    # 显示地区数据
    st.dataframe(regions_data, use_container_width=True)
    
    # 可视化分析
    st.subheader("📊 地区特征分析")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 物流成本vs订单量散点图
        cost_volume_chart = alt.Chart(regions_data).mark_circle(size=100).encode(
            x=alt.X('order_volume:Q', title='月订单量'),
            y=alt.Y('logistics_cost:Q', title='物流成本(元/单)'),
            color=alt.Color('region:N', scale=alt.Scale(scheme='category20')),
            tooltip=['region:N', 'order_volume:Q', 'logistics_cost:Q']
        ).properties(
            height=300,
            title='物流成本 vs 订单量'
        )
        st.altair_chart(cost_volume_chart, use_container_width=True)
        
        # 配送时长vs满意度
        time_satisfaction_chart = alt.Chart(regions_data).mark_circle(size=100).encode(
            x=alt.X('delivery_time:Q', title='平均配送时长(天)'),
            y=alt.Y('user_satisfaction:Q', title='用户满意度'),
            color=alt.Color('region:N', scale=alt.Scale(scheme='category20')),
            tooltip=['region:N', 'delivery_time:Q', 'user_satisfaction:Q']
        ).properties(
            height=300,
            title='配送时长 vs 用户满意度'
        )
        st.altair_chart(time_satisfaction_chart, use_container_width=True)
    
    with col2:
        # 人口vs订单量
        pop_order_chart = alt.Chart(regions_data).mark_bar().encode(
            x=alt.X('region:N', title='地区', sort=None),
            y=alt.Y('population:Q', title='人口(万人)'),
            color=alt.value('#4ECDC4'),
            tooltip=['region:N', 'population:Q']
        ).properties(
            height=300,
            title='地区人口分布'
        )
        st.altair_chart(pop_order_chart, use_container_width=True)
        
        # 人均GDP vs 订单量
        gdp_order_chart = alt.Chart(regions_data).mark_circle(size=100).encode(
            x=alt.X('gdp_per_capita:Q', title='人均GDP(万元)'),
            y=alt.Y('order_volume:Q', title='月订单量'),
            color=alt.Color('region:N', scale=alt.Scale(scheme='category20')),
            tooltip=['region:N', 'gdp_per_capita:Q', 'order_volume:Q']
        ).properties(
            height=300,
            title='人均GDP vs 订单量'
        )
        st.altair_chart(gdp_order_chart, use_container_width=True)
    
    # 统计显著性检验详解
    st.subheader("🔬 统计显著性检验详解")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 订单量检验 (t-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用t-test？</strong>订单量是连续变量，t-test适用于连续数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                t = (x̄₁ - x̄₂) / s_p√(1/n₁ + 1/n₂)
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组订单量：1.38万单 ± 0.15</li>
                <li>对照组订单量：1.20万单 ± 0.12</li>
                <li>t统计量：6.8</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">📈 满意度检验 (t-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用t-test？</strong>满意度是连续变量（0-1评分），t-test适用于连续数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                t = (x̄₁ - x̄₂) / s_p√(1/n₁ + 1/n₂)
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组满意度：0.77 ± 0.08</li>
                <li>对照组满意度：0.72 ± 0.09</li>
                <li>t统计量：4.2</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">⏱️ 配送时长检验 (t-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用t-test？</strong>配送时长是连续变量（天数），t-test适用于连续数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                t = (x̄₁ - x̄₂) / s_p√(1/n₁ + 1/n₂)
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组配送时长：4.2 ± 0.8天</li>
                <li>对照组配送时长：5.2 ± 1.2天</li>
                <li>t统计量：-5.6</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 统计检验结果汇总
    st.markdown("### 📋 统计检验结果汇总")
    
    test_results = pd.DataFrame({
        '指标': ['月订单量', '用户满意度', '配送时长', 'GMV增长率'],
        '实验组': ['1.38万单', '77%', '4.2天', '+28%'],
        '对照组': ['1.20万单', '72%', '5.2天', '+15%'],
        '提升幅度': ['+15%', '+5%', '-1.0天', '+13%'],
        'p值': ['<0.001', '<0.001', '<0.001', '<0.001'],
        '显著性': ['***', '***', '***', '***']
    })
    
    st.dataframe(test_results, use_container_width=True)
    
    # 结果解读与业务落地
    st.subheader("🎯 结果解读与业务落地")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 统计显著性</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>所有核心指标p<0.001</li>
                <li>远小于α=0.05</li>
                <li>拒绝零假设</li>
                <li>结果可信度高</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">💼 业务显著性</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>订单量：1.20→1.38万单（+15%）</li>
                <li>满意度：72%→77%（+5%）</li>
                <li>配送时长：5.2→4.2天（-19%）</li>
                <li>均远超MDE阈值</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #7b1fa2; margin: 0 0 10px 0;">🧠 业务解释力</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>区域配送中心提升效率</li>
                <li>批量配送降低成本</li>
                <li>专业服务提升体验</li>
                <li>市场空白带来增长</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # AB测试结论与决策
    st.subheader("🎯 AB测试结论与决策")
    
    st.markdown("""
    <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #2e7d32; margin: 0 0 10px 0;">✅ AB测试结论</h4>
        <p style="color: #424242; margin: 0;">
            基于90天AB测试结果，<strong>偏远地区物流业务整体ROI为正</strong>，建议开展。
            但不同地区表现差异显著，需要<strong>分地区精细化运营</strong>。
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 分地区ROI分析
    st.subheader("📊 分地区ROI详细分析")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">🎯 分析目标</h4>
        <p style="color: #424242; margin: 0;">
            在确认整体策略有效后，深入分析各地区的具体表现，制定<strong>分地区优先级策略</strong>。
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 地区ROI排名分析
    st.markdown("### 🏆 地区ROI排名分析")
    
    # 模拟分地区ROI数据
    regional_roi_analysis = pd.DataFrame({
        '地区': ['内蒙古', '青海', '甘肃', '新疆', '云南', '贵州', '广西', '海南', '宁夏', '西藏'],
        '月订单量(万单)': [1.8, 0.85, 1.5, 1.2, 3.5, 2.8, 4.5, 1.5, 0.42, 0.28],
        '物流成本(元/单)': [6.2, 7.8, 7.1, 8.5, 5.9, 6.5, 5.7, 6.1, 6.8, 12.3],
        '基础设施投入(万元)': [200, 300, 350, 500, 400, 450, 600, 250, 150, 800],
        'GMV增长(%)': [35, 30, 28, 25, 32, 28, 30, 25, 20, 15],
        '用户LTV提升(%)': [30, 25, 22, 20, 28, 25, 27, 22, 18, 12],
        'ROI(倍)': [4.5, 3.2, 2.8, 2.1, 3.8, 2.9, 3.5, 2.6, 2.2, 0.8],
        '优先级': ['强烈推荐', '推荐', '推荐', '推荐', '强烈推荐', '推荐', '强烈推荐', '推荐', '推荐', '暂缓']
    })
    
    st.dataframe(regional_roi_analysis, use_container_width=True)
    
    # ROI分析可视化
    st.markdown("### 📈 ROI分析可视化")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # ROI vs 订单量散点图
        roi_scatter = alt.Chart(regional_roi_analysis).mark_circle(size=100).encode(
            x=alt.X('月订单量(万单):Q', title='月订单量(万单)'),
            y=alt.Y('ROI(倍):Q', title='ROI(倍)'),
            color=alt.Color('优先级:N', scale=alt.Scale(range=['#ff6b6b', '#4ecdc4', '#45b7d1'])),
            tooltip=['地区:N', '月订单量(万单):Q', 'ROI(倍):Q', '优先级:N']
        ).properties(
            height=300,
            title='订单量 vs ROI 分析'
        )
        st.altair_chart(roi_scatter, use_container_width=True)
    
    with col2:
        # 成本 vs ROI散点图
        cost_roi_scatter = alt.Chart(regional_roi_analysis).mark_circle(size=100).encode(
            x=alt.X('物流成本(元/单):Q', title='物流成本(元/单)'),
            y=alt.Y('ROI(倍):Q', title='ROI(倍)'),
            color=alt.Color('优先级:N', scale=alt.Scale(range=['#ff6b6b', '#4ecdc4', '#45b7d1'])),
            tooltip=['地区:N', '物流成本(元/单):Q', 'ROI(倍):Q', '优先级:N']
        ).properties(
            height=300,
            title='物流成本 vs ROI 分析'
        )
        st.altair_chart(cost_roi_scatter, use_container_width=True)
    
    # 地区优先级决策矩阵
    st.markdown("### 🎯 地区优先级决策矩阵")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">🚀 强烈推荐地区</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>内蒙古</strong>：ROI 4.5倍，订单量大，成本低</li>
                <li><strong>云南</strong>：ROI 3.8倍，订单量最大，增长潜力大</li>
                <li><strong>广西</strong>：ROI 3.5倍，订单量最大，地理位置优越</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">⚠️ 暂缓地区</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>西藏</strong>：ROI 0.8倍，成本过高，订单量小</li>
                <li><strong>宁夏</strong>：ROI 2.2倍，订单量过小，规模效应不足</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 实施建议
    st.markdown("### 💡 分阶段实施建议")
    
    st.markdown("""
    <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #7b1fa2; margin: 0 0 10px 0;">📋 三阶段实施策略</h4>
        <ol style="color: #424242; margin: 0; padding-left: 20px;">
            <li><strong>第一阶段（立即实施）</strong>：内蒙古、云南、广西 - 高ROI+大订单量</li>
            <li><strong>第二阶段（3个月后）</strong>：青海、甘肃、新疆、贵州、海南 - 中等ROI</li>
            <li><strong>第三阶段（6个月后）</strong>：宁夏 - 小规模试点，西藏 - 暂缓或重新评估</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # 项目成果总结
    st.subheader("🏆 项目成果总结")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("整体ROI", "2.8倍", "+180%")
    with col2:
        st.metric("推荐地区数", "8个", "80%")
    with col3:
        st.metric("预期GMV增长", "+28%", "显著提升")
    
    # 关键学习点
    st.markdown("### 💡 关键学习点")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">🎯 核心洞察</h4>
        <ul style="color: #424242; margin: 0; padding-left: 20px;">
            <li><strong>AB测试验证</strong>：偏远地区物流业务整体ROI为正，策略有效</li>
            <li><strong>地区差异显著</strong>：不同地区ROI差异巨大，需要精细化运营</li>
            <li><strong>规模效应重要</strong>：订单量大的地区更容易实现规模经济</li>
            <li><strong>成本控制关键</strong>：物流成本是影响ROI的核心因素</li>
            <li><strong>分阶段实施</strong>：优先高ROI地区，逐步扩展到其他地区</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 实施建议
    st.markdown("""
    <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #7b1fa2; margin: 0 0 10px 0;">🚀 实施建议</h4>
        <ol style="color: #424242; margin: 0; padding-left: 20px;">
            <li><strong>分阶段推进</strong>：优先开展ROI高的地区</li>
            <li><strong>成本控制</strong>：与当地物流商建立合作关系</li>
            <li><strong>用户体验</strong>：设置合理的配送时效预期</li>
            <li><strong>持续监控</strong>：建立实时数据监控体系</li>
            <li><strong>动态调整</strong>：根据实际效果调整策略</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ---------------- Page 7: MTA归因模型项目 ---------------- 
elif page == "Work in Progress":
    # 密码验证
    st.markdown("### 🔐 访问验证")
    password = st.text_input("请输入访问密码", type="password")
    
    if password != "MTA2024":
        st.error("❌ 密码错误，无法访问此页面")
        st.stop()
    
    st.success("✅ 验证成功，欢迎访问MTA归因模型项目")
    st.header("🎯 MTA归因模型项目 - AB测试与预算分配深度解析")
    
    # 项目背景（简化）
    st.subheader("📋 项目背景")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">🏥 UnitedHealthcare (UHG) - 1亿美元广告预算优化</h4>
        <p style="color: #424242; margin: 0;">
            <strong>核心挑战：</strong>Last Click归因显示付费搜索贡献65%，但用户决策周期45-60天，前端渠道价值被严重低估<br>
            <strong>解决方案：</strong>构建Shapley Value归因模型，通过AB测试验证，重新分配预算<br>
            <strong>AB测试规模：</strong>总预算的2%用于测试（$200万），验证模型效果后全量推广
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Shapley Value结果（简化展示）
    st.subheader("📊 Shapley Value归因结果")
    
    # 创建双色柱状图
    comparison_data = pd.DataFrame({
        '渠道类型': ['Paid Search', 'Social Media', 'Display', 'Affiliate'],
        'Last Click贡献(%)': [65, 8, 5, 22],
        'Shapley值贡献(%)': [45, 18, 15, 22],
        '差异(%)': [-20, +10, +10, 0]
    })
    
    # 转换为长格式用于绘图
    comparison_long = comparison_data.melt(
        id_vars=['渠道类型'], 
        value_vars=['Last Click贡献(%)', 'Shapley值贡献(%)'],
        var_name='模型类型', 
        value_name='贡献度(%)'
    )
    
    # 创建分组柱状图
    comparison_chart = alt.Chart(comparison_long).mark_bar().encode(
        x=alt.X('渠道类型:N', sort=None),
        y=alt.Y('贡献度(%):Q'),
        color=alt.Color('模型类型:N', scale=alt.Scale(range=['#ff6b6b', '#4ecdc4'])),
        tooltip=['渠道类型:N', '模型类型:N', '贡献度(%):Q']
    ).properties(
        height=300,
        title='Last Click vs Shapley Value 贡献度对比'
    ).resolve_scale(
        x='independent'
    )
    
    st.altair_chart(comparison_chart, use_container_width=True)
    
    # AB测试设计 - 详细解析
    st.subheader("🧪 AB测试设计详解")
    
    # 用户选择策略
    st.markdown("### 🎯 用户选择与分组策略")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">👥 用户选择标准</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>年龄</strong>：25-60岁（商业保险主要用户）</li>
                <li><strong>收入</strong>：年收入$40K-$120K</li>
                <li><strong>地区</strong>：10个州，每州选择相似城市</li>
                <li><strong>行为</strong>：过去6个月有保险相关搜索</li>
                <li><strong>排除</strong>：已有UHG保险的用户</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">🎲 随机分组方法</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>分层随机</strong>：按州、年龄、收入分层，确保每组在各维度分布相似</li>
                <li><strong>哈希算法</strong>：user_id % 2 确保同一用户始终在同一组，避免分组漂移</li>
                <li><strong>样本量</strong>：每组10万用户（合计20万）</li>
                <li><strong>测试预算</strong>：每组$100万（总$200万）</li>
                <li><strong>时间窗口</strong>：60天实验周期（符合45-60天决策周期）</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 样本量计算
    st.markdown("### 📊 样本量计算")
    
    st.markdown("""
    <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #2e7d32; margin: 0 0 10px 0;">🧮 功效分析计算</h4>
        <p style="color: #424242; margin: 0;">
            <strong>基于历史数据</strong>：原模型下转化率0.1%、CPA $280
        </p>
        <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
            <li><strong>α=0.05</strong>：假阳性率（5%显著性水平）</li>
            <li><strong>1-β=0.8</strong>：80%检测效力</li>
            <li><strong>MDE</strong>：转化率提升0.05%、CPA下降10%</li>
            <li><strong>最终确定</strong>：每组覆盖10万用户（合计20万）</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 分组平衡性检验
    st.markdown("### ⚖️ 分组平衡性检验")
    
    balance_data = pd.DataFrame({
        '特征': ['平均年龄', '平均收入($K)', '男性比例(%)', '城市用户比例(%)', '过去搜索次数'],
        '实验组': [42.3, 68.5, 51.2, 78.4, 4.2],
        '对照组': [42.1, 68.2, 50.8, 78.1, 4.3],
        '差异': [0.2, 0.3, 0.4, 0.3, -0.1],
        'p值': [0.85, 0.72, 0.68, 0.91, 0.76],
        '结论': ['平衡', '平衡', '平衡', '平衡', '平衡']
    })
    
    st.dataframe(balance_data, use_container_width=True)
    
    # 实验设计详情
    st.markdown("### 📋 实验设计详情")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">🎯 实验组策略 ($100万预算)</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>Paid Search</strong>：$70万 → $45万 (-$25万)</li>
                <li><strong>Display</strong>：$15万 → $15万 (0)</li>
                <li><strong>Social Media</strong>：$10万 → $18万 (+$8万)</li>
                <li><strong>Affiliate</strong>：$5万 → $22万 (+$17万)</li>
                <li><strong>总预算</strong>：$100万 (保持不变)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">📊 对照组策略 ($100万预算)</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>Paid Search</strong>：$65万 (65%基准，Last Click权重)</li>
                <li><strong>Display</strong>：$5万 (5%基准，Last Click权重)</li>
                <li><strong>Social Media</strong>：$8万 (8%基准，Last Click权重)</li>
                <li><strong>Affiliate</strong>：$22万 (22%基准，Last Click权重)</li>
                <li><strong>总预算</strong>：$100万 (保持不变)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 显著性检验详解
    st.subheader("🔬 统计显著性检验详解")
    
    # 模拟AB测试数据
    np.random.seed(42)
    n_users = 500000  # 每组50万用户
    
    # 实验组数据
    treatment_data = {
        'conversions': np.random.binomial(1, 0.002, n_users),  # 0.2%转化率
        'revenue': np.random.normal(1200, 200, n_users),  # 平均收入$1200
        'cost': np.random.normal(200, 20, n_users),  # 平均成本$200
        'group': '实验组'
    }
    
    # 对照组数据
    control_data = {
        'conversions': np.random.binomial(1, 0.001, n_users),  # 0.1%转化率
        'revenue': np.random.normal(1000, 180, n_users),  # 平均收入$1000
        'cost': np.random.normal(280, 25, n_users),  # 平均成本$280
        'group': '对照组'
    }
    
    # 合并数据
    ab_test_data = pd.DataFrame({
        'conversions': np.concatenate([treatment_data['conversions'], control_data['conversions']]),
        'revenue': np.concatenate([treatment_data['revenue'], control_data['revenue']]),
        'cost': np.concatenate([treatment_data['cost'], control_data['cost']]),
        'group': ['实验组'] * n_users + ['对照组'] * n_users
    })
    
    # 计算关键指标
    treatment_conv_rate = ab_test_data[ab_test_data['group'] == '实验组']['conversions'].mean()
    control_conv_rate = ab_test_data[ab_test_data['group'] == '对照组']['conversions'].mean()
    treatment_cpa = ab_test_data[ab_test_data['group'] == '实验组']['cost'].mean()
    control_cpa = ab_test_data[ab_test_data['group'] == '对照组']['cost'].mean()
    treatment_roas = ab_test_data[ab_test_data['group'] == '实验组']['revenue'].mean() / ab_test_data[ab_test_data['group'] == '实验组']['cost'].mean()
    control_roas = ab_test_data[ab_test_data['group'] == '对照组']['revenue'].mean() / ab_test_data[ab_test_data['group'] == '对照组']['cost'].mean()
    
    # 关键指标对比
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "转化率", 
            f"{treatment_conv_rate:.3%}", 
            f"{(treatment_conv_rate - control_conv_rate):.3%}"
        )
    
    with col2:
        st.metric(
            "CPA", 
            f"${treatment_cpa:.0f}", 
            f"-${control_cpa - treatment_cpa:.0f}"
        )
    
    with col3:
        st.metric(
            "ROAS", 
            f"{treatment_roas:.1f}x", 
            f"+{treatment_roas - control_roas:.1f}x"
        )
    
    # 详细统计检验
    st.markdown("### 📊 统计检验过程")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">🧮 转化率检验 (Z-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用Z-test？</strong>转化率是二分类变量（转化/不转化），Z-test适用于比例数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                Z = (p₁ - p₀) / √(p(1-p)(1/n₁ + 1/n₀))
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组转化数：1,000</li>
                <li>对照组转化数：500</li>
                <li>Z统计量：15.8</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">📈 CPA检验 (t-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用t-test？</strong>CPA是连续变量（美元金额），t-test适用于连续数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                t = (x̄₁ - x̄₂) / s_p√(1/n₁ + 1/n₂)
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组CPA：$200 ± $20</li>
                <li>对照组CPA：$280 ± $25</li>
                <li>t统计量：-12.5</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">💰 ROAS检验 (t-test)</h4>
            <p style="color: #424242; margin: 0; font-size: 12px; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                <strong>为什么用t-test？</strong>ROAS是连续变量（收入/成本比值），t-test适用于连续数据
            </p>
            <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
                t = (x̄₁ - x̄₂) / s_p√(1/n₁ + 1/n₂)
            </p>
            <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
                <li>实验组ROAS：3.2x ± 0.3</li>
                <li>对照组ROAS：2.1x ± 0.2</li>
                <li>t统计量：8.7</li>
                <li>p值：< 0.001</li>
                <li>结论：高度显著</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 统计检验结果表
    st.markdown("### 📋 统计检验结果汇总")
    
    test_results = pd.DataFrame({
        '指标': ['转化率', 'CPA', 'ROAS', '总收入'],
        '实验组': ['0.200%', '$200', '6.0x', '$1.2M'],
        '对照组': ['0.100%', '$280', '3.6x', '$1.0M'],
        '提升幅度': ['+100%', '-28.6%', '+66.7%', '+20%'],
        '统计量': ['Z=15.8', 't=-12.5', 't=8.2', 't=5.1'],
        'p值': ['<0.001', '<0.001', '<0.001', '<0.001'],
        '显著性': ['***', '***', '***', '***']
    })
    
    st.dataframe(test_results, use_container_width=True)
    
    # # 效应量分析
    # st.markdown("### 📊 效应量分析 (Cohen's d)")
    
    # st.markdown("""
    # <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 15px 0;">
    #     <h4 style="color: #f57c00; margin: 0 0 10px 0;">💡 什么是效应量？</h4>
    #     <p style="color: #424242; margin: 0;">
    #         效应量评估实际业务意义，不仅仅是统计显著性。Cohen's d > 0.5表示中等效应，> 0.8表示大效应。
    #         即使统计显著，如果效应量很小，实际业务价值可能有限。
    #     </p>
    # </div>
    # """, unsafe_allow_html=True)
    
    # col1, col2, col3 = st.columns(3)
    
    # with col1:
    #     st.metric("转化率效应量", "0.45", "中等效应")
    # with col2:
    #     st.metric("CPA效应量", "-0.38", "中等效应")
    # with col3:
    #     st.metric("ROAS效应量", "0.52", "大效应")
    
    # 结果解读与业务落地
    st.subheader("🎯 结果解读与业务落地")
    
    # st.markdown("""
    # <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
    #     <h4 style="color: #1976d2; margin: 0 0 10px 0;">🏢 国内大厂决策框架</h4>
    #     <p style="color: #424242; margin: 0;">
    #         国内大厂不会只看p值，会结合<strong>统计显著性 + 业务显著性 + 模型解释力</strong>做决策：
    #     </p>
    # </div>
    # """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 统计显著性</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>所有核心指标p<0.001</li>
                <li>远小于α=0.05</li>
                <li>拒绝零假设</li>
                <li>结果可信度高</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #f57c00; margin: 0 0 10px 0;">💼 业务显著性</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>转化率：0.1%→0.2%（翻倍）</li>
                <li>CPA：280→200（-28%）</li>
                <li>ROAS：2.1→3.2（+52%）</li>
                <li>均远超MDE阈值</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #7b1fa2; margin: 0 0 10px 0;">🧠 模型解释力</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li>Display+Search协同转化概率高40%</li>
                <li>Social"种草"效应被量化</li>
                <li>转化率提升17%</li>
                <li>Shapley模型正确性验证</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # # 预算重分配决策模型详解
    # st.subheader("💰 预算重分配决策模型详解")
    
    # st.markdown("""
    # <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 15px 0;">
    #     <h4 style="color: #1976d2; margin: 0 0 10px 0;">🎯 为什么需要复杂的预算优化？</h4>
    #     <p style="color: #424242; margin: 0;">
    #         虽然Shapley值给出了理论最优分配，但实际业务需要考虑：
    #     </p>
    #     <ul style="color: #424242; margin: 10px 0 0 0; padding-left: 20px;">
    #         <li><strong>业务约束</strong>：Paid Search不能低于30%（品牌安全）</li>
    #         <li><strong>容量限制</strong>：某些渠道有投放上限</li>
    #         <li><strong>风险控制</strong>：避免过度依赖单一渠道</li>
    #         <li><strong>协同效应</strong>：渠道间相互影响</li>
    #     </ul>
    # </div>
    # """, unsafe_allow_html=True)
    
    # # 边际ROI计算
    # st.markdown("### 📊 边际ROI计算过程")
    
    # col1, col2 = st.columns(2)
    
    # with col1:
    #     st.markdown("""
    #     <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
    #         <h4 style="color: #2e7d32; margin: 0 0 10px 0;">🧮 边际ROI公式</h4>
    #         <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
    #             Marginal_ROI_i = (ΔRevenue_i / ΔCost_i) × Shapley_Weight_i<br>
    #             其中：<br>
    #             • ΔRevenue_i = 渠道i的边际收入贡献<br>
    #             • ΔCost_i = 渠道i的边际成本<br>
    #             • Shapley_Weight_i = 渠道i的Shapley权重
    #         </p>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # with col2:
    #     st.markdown("""
    #     <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
    #         <h4 style="color: #1976d2; margin: 0 0 10px 0;">📈 协同效应调整</h4>
    #         <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
    #             Synergy_Bonus_i = Σ(Interaction_Effect_ij × Budget_j)<br>
    #             其中：<br>
    #             • Interaction_Effect_ij = 渠道i与j的协同系数<br>
    #             • Budget_j = 渠道j的预算分配
    #         </p>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # # 边际ROI计算示例
    # st.markdown("### 📋 各渠道边际ROI计算")
    
    # marginal_roi_data = pd.DataFrame({
    #     '渠道': ['Paid Search', 'Display', 'Social Media', 'Affiliate'],
    #     'Shapley权重': [0.32, 0.20, 0.22, 0.26],
    #     '边际收入($)': [1200, 800, 900, 1000],
    #     '边际成本($)': [280, 200, 180, 250],
    #     '基础ROI': [4.29, 4.00, 5.00, 4.00],
    #     '协同系数': [0.15, 0.35, 0.30, 0.10],
    #     '调整后ROI': [4.93, 5.40, 6.50, 4.40],
    #     '预算建议': ['减少', '增加', '增加', '保持']
    # })
    
    # st.dataframe(marginal_roi_data, use_container_width=True)
    
    # 预算优化算法
    # st.markdown("### 🎯 预算优化算法实现")
    
    # col1, col2 = st.columns(2)
    
    # with col1:
    #     st.markdown("""
    #     <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 10px 0;">
    #         <h4 style="color: #f57c00; margin: 0 0 10px 0;">🔧 优化目标函数</h4>
    #         <p style="color: #424242; margin: 0; font-family: monospace; background: #f5f5f5; padding: 10px; border-radius: 4px;">
    #             max Σ(Adjusted_ROI_i × Budget_i)<br>
    #             s.t. Σ(Budget_i) = $100M<br>
    #             &nbsp;&nbsp;&nbsp;&nbsp;Budget_i ≥ Min_Threshold_i<br>
    #             &nbsp;&nbsp;&nbsp;&nbsp;Budget_i ≤ Max_Capacity_i
    #         </p>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # with col2:
    #     st.markdown("""
    #     <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 15px; border-radius: 4px; margin: 10px 0;">
    #         <h4 style="color: #7b1fa2; margin: 0 0 10px 0;">⚙️ 约束条件</h4>
    #         <ul style="color: #424242; margin: 0; padding-left: 20px;">
    #             <li><strong>最小阈值</strong>：Search≥$30M, Display≥$10M</li>
    #             <li><strong>最大容量</strong>：Social≤$30M, Affiliate≤$15M</li>
    #             <li><strong>品牌安全</strong>：Search占比≥30%</li>
    #             <li><strong>季节性</strong>：Q4预算调整±20%</li>
    #         </ul>
    #     </div>
    #     """, unsafe_allow_html=True)
    
    # 具体预算削减计算逻辑
    st.markdown("### 💰 预算削减计算逻辑详解")
    
    # 为什么削减2500万的计算过程
    st.markdown("#### 🧮 为什么削减Paid Search 2500万美元？")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 计算依据</h4>
            <ol style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>Shapley权重</strong>：Paid Search = 45%</li>
                <li><strong>理论预算</strong>：$100M × 45% = $45M</li>
                <li><strong>业务约束</strong>：Search占比≥30% = $30M</li>
                <li><strong>最终预算</strong>：max($45M, $30M) = $45M</li>
                <li><strong>削减金额</strong>：$70M - $45M = $25M</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; border-radius: 4px; margin: 10px 0;">
            <h4 style="color: #1976d2; margin: 0 0 10px 0;">⚖️ 约束条件</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px;">
                <li><strong>最小Search预算</strong>：$30M (30%)</li>
                <li><strong>品牌安全要求</strong>：Search占比≥30%</li>
                <li><strong>渠道容量限制</strong>：Social≤$30M</li>
                <li><strong>季节性调整</strong>：Q4预算±20%</li>
                <li><strong>风险控制</strong>：单渠道变化≤25%</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 详细计算过程
    st.markdown("#### 📋 详细计算过程")
    
    calculation_steps = pd.DataFrame({
        '步骤': ['Shapley权重分析', '理论预算计算', '约束条件应用', '最终预算分配', '预算变化'],
        'Paid Search': ['45%', '$45M', '$45M (≥30%)', '$45M', '-$25M'],
        'Display': ['15%', '$15M', '$15M', '$15M', '$0M'],
        'Social Media': ['18%', '$18M', '$18M', '$18M', '+$8M'],
        'Affiliate': ['22%', '$22M', '$22M', '$22M', '+$17M'],
        '说明': [
            'Shapley Value归因结果',
            '按权重分配预算',
            '应用业务约束条件',
            '最终优化分配',
            '相比原预算的变化'
        ]
    })
    
    st.dataframe(calculation_steps, use_container_width=True)
    
    # # 预算优化算法实现
    # st.markdown("#### 🎯 预算优化算法实现")
    
    # st.markdown("""
    # <div style="background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 15px; border-radius: 4px; margin: 15px 0;">
    #     <h4 style="color: #f57c00; margin: 0 0 10px 0;">🔧 优化算法步骤</h4>
    #     <ol style="color: #424242; margin: 0; padding-left: 20px;">
    #         <li><strong>计算理论预算</strong>：Budget_i = Total_Budget × Shapley_Weight_i</li>
    #         <li><strong>应用最小约束</strong>：Budget_i = max(Budget_i, Min_Threshold_i)</li>
    #         <li><strong>应用最大约束</strong>：Budget_i = min(Budget_i, Max_Capacity_i)</li>
    #         <li><strong>重新归一化</strong>：Budget_i = Budget_i × (Total_Budget / ΣBudget_i)</li>
    #         <li><strong>验证约束</strong>：确保所有约束条件满足</li>
    #     </ol>
    # </div>
    # """, unsafe_allow_html=True)
    
    # # 预算分配决策树
    # st.markdown("### 🌳 预算分配决策树")
    
    # decision_tree_data = pd.DataFrame({
    #     '决策节点': ['Shapley权重>20%', '边际ROI>4.0', '协同效应>0.3', '风险评级<中', '容量约束'],
    #     'Paid Search': ['是', '是', '否', '是', '是'],
    #     'Display': ['是', '是', '是', '是', '是'],
    #     'Social Media': ['是', '是', '是', '是', '否'],
    #     'Affiliate': ['是', '是', '否', '是', '是'],
    #     '决策结果': ['保持', '增加', '增加', '减少', '调整']
    # })
    
    # st.dataframe(decision_tree_data, use_container_width=True)
    
    # # 最终预算分配方案
    # st.markdown("### 📋 最终预算分配方案")
    
    # final_budget_data = pd.DataFrame({
    #     '渠道': ['Paid Search', 'Display', 'Social Media', 'Affiliate', '总计'],
    #     '原预算(万美元)': [7000, 1500, 1000, 500, 10000],
    #     '新预算(万美元)': [4500, 1500, 1800, 2200, 10000],
    #     '变化(万美元)': [-2500, 0, +800, +1700, 0],
    #     '变化幅度': ['-35.7%', '0%', '+80.0%', '+340.0%', '0%'],
    #     'Shapley权重': ['45%', '15%', '18%', '22%', '100%'],
    #     '调整后权重': ['45%', '15%', '18%', '22%', '100%'],
    #     '预期ROI': ['4.9x', '5.4x', '6.5x', '4.4x', '4.1x'],
    #     '调整理由': [
    #         'Shapley权重显示适度高估，合理削减',
    #         '长期种草效应显著，保持健康科普视频投放',
    #         'KOL合作效果突出，重点投入商业保险内容',
    #         '比价/测评环节价值被低估，大幅增加投放',
    #         '整体ROI提升28%'
    #     ]
    # })
    
    # st.dataframe(final_budget_data, use_container_width=True)
    
    # # AB测试验证后的全量推广
    # st.markdown("### 🚀 AB测试验证后的全量推广")
    
    # st.markdown("""
    # <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 15px; border-radius: 4px; margin: 15px 0;">
    #     <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📈 推广策略</h4>
    #     <ul style="color: #424242; margin: 0; padding-left: 20px;">
    #         <li><strong>AB测试结果</strong>：转化率提升100%，CPA降低28.6%，ROAS提升52.4%</li>
    #         <li><strong>推广范围</strong>：从2%测试用户扩展到100%全量用户</li>
    #         <li><strong>预算规模</strong>：从$200万测试预算扩展到$1亿全量预算</li>
    #         <li><strong>风险控制</strong>：分阶段推广，每阶段监控关键指标</li>
    #         <li><strong>预期收益</strong>：年化ROI提升28%，节省成本$2800万</li>
    #     </ul>
    # </div>
    # """, unsafe_allow_html=True)
    
    # 项目成果总结
    st.subheader("🏆 项目成果总结")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("转化率提升", "0.1% → 0.2%", "+100%")
    with col2:
        st.metric("CPA降低", "$280 → $200", "-28.6%")
    with col3:
        st.metric("ROAS提升", "2.1x → 3.2x", "+52.4%")
    
    # 关键学习点
    st.markdown("### 💡 关键学习点")
    
    st.markdown("""
    <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 20px; border-radius: 4px; margin: 15px 0;">
        <h4 style="color: #7b1fa2; margin: 0 0 15px 0;">🎯 核心洞察</h4>
        <ol style="color: #424242; margin: 0; padding-left: 20px;">
            <li><strong>AB测试设计</strong>：分层随机确保组间平衡，大样本量保证统计功效</li>
            <li><strong>显著性检验</strong>：Z-test用于比例，t-test用于连续变量，效应量评估实际意义</li>
            <li><strong>预算优化</strong>：边际ROI + Shapley权重 + 协同效应 = 最优分配</li>
            <li><strong>业务约束</strong>：技术模型需结合业务现实，平衡理想与可行</li>
            <li><strong>持续监控</strong>：模型需要定期重校准，适应市场变化</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; margin-top: 2rem; color: #666; font-size: 14px;">
        Demo by 侯良语 | 2025-09-27
    </div>
    """, 
    unsafe_allow_html=True
)