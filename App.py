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

page = st.sidebar.radio("页面", ["说明", "对比与发展", "履约指标决策树", "平台/商家/用户可视化"], index=0)
st.sidebar.markdown(
    """
    <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; margin: 10px 0;">
        <h4 style="color: #1976d2; margin: 0 0 10px 0;">📋 术语说明</h4>
        <p style="margin: 5px 0; color: #424242;"><strong>平台</strong> = 抖音电商</p>
        <p style="margin: 5px 0; color: #424242;"><strong>商家</strong> = 入驻抖音卖货的商家</p>
        <p style="margin: 5px 0; color: #424242;"><strong>用户</strong> = 抖音购物用户</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# ---------------- Page 1: 说明 ----------------
if page == "说明":
    # st.header("说明")
    st.markdown(
        """
        <div style="background-color: #e8f5e8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #4caf50;">
            <h3 style="color: #2e7d32; margin: 0 0 15px 0;">🎯 目标</h3>
            <p style="color: #424242; margin: 10px 0; font-size: 16px;">
                该Demo旨在通过对以下三个维度的分析，展示候选人对业务和岗位内容的快速学习和理解能力：
            </p>
            <ol style="color: #424242; margin: 15px 0; padding-left: 20px;">
                <li style="margin: 8px 0;">📈 抖音物流的发展历程</li>
                <li style="margin: 8px 0;">🎯 抖音电商物流履约指标体系</li>
                <li style="margin: 8px 0;">📊 平台/商家/用户视角分析的可视化</li>
            </ol>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
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
    st.subheader("📊 横向对比：抖音 vs 京东 / 淘宝 / 小红书")
    
    # 美化对比表格
    comp_data = {
        "平台": ["抖音电商", "京东", "淘宝/天猫", "小红书"],
        "物流模式摘要": [
            "轻资产模式+字节面单系统；音尊达/云仓/抖音超市等多元化尝试；2024年战略调整，下线部分服务。",
            "自营+京东物流为核心，仓储网点密集、时效稳定；适合时效敏感型品类。",
            "天猫/淘宝生态中商家+菜鸟/快递公司组合，平台提供运力协同与履约保障工具。",
            "以内容社区导购为主，电商还在发展中，物流多依赖第三方商家与快递。"
        ],
        "对比要点": [
            "内容->交易，物流控制力逐步增强但仍有局限",
            "重资产物流，端到端掌控力强",
            "成熟的商家履约规则与赔付机制",
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
        'platform': ['抖音','京东','淘宝','小红书'],
        '配送时效': [60,90,80,55],
        '平台控制力': [50,95,80,45]
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

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; margin-top: 2rem; color: #666; font-size: 14px;">
        Demo by 侯良语 | 2025-09-25
    </div>
    """, 
    unsafe_allow_html=True
)