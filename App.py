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

page = st.sidebar.radio("页面", ["说明", "🔥 双11专题", "对比与发展", "履约指标决策树", "平台/商家/用户可视化", "优质快递体验验证", "偏远地区物流验证", "MTA归因模型AB测试"], index=0)

# ---------------- Page 1: 说明 ----------------
if page == "说明":
    # 给面试官的复工互动 🐂🐴
    if 'niuma_clicked' not in st.session_state:
        st.session_state.niuma_clicked = False
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if not st.session_state.niuma_clicked:
            # 默认状态：累了吧唧的牛马
            st.markdown("""
            <div style="text-align: center; padding: 15px; background-color: #e0e0e0; 
                        border-radius: 10px; margin: 10px 0;">
                <div style="font-size: 60px; margin-bottom: 5px;">🐂🐴</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("点我 ", use_container_width=True, key="niuma_btn"):
                st.session_state.niuma_clicked = True
                st.rerun()
        else:
            # 点击后：复工快乐！
            st.markdown("""
            <div style="text-align: center; padding: 15px; background-color: #fff8e1; 
                        border-radius: 10px; margin: 10px 0; border-left: 4px solid #ffc107;">
                <div style="font-size: 60px; margin-bottom: 5px;">🎉</div>
                <p style="color: #f57c00; font-size: 18px; font-weight: bold; margin: 0;">复工快乐！</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("💪 加油！（再点返回）", use_container_width=True, key="niuma_btn2"):
                st.session_state.niuma_clicked = False
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="background-color: #e8f5e8; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #4caf50;">
            <h3 style="color: #2e7d32; margin: 0 0 15px 0;">🎯 目标</h3>
            <p style="color: #424242; margin: 10px 0; font-size: 16px;">
                该Demo旨在展示候选人对<strong>抖音电商物流业务</strong>的快速学习和理解能力，涵盖：
            </p>
            <ol style="color: #424242; margin: 15px 0; padding-left: 20px; line-height: 2;">
                <li style="margin: 10px 0;"><strong>🔥 双11专题（重点）</strong>
                    <ul style="font-size: 14px; margin: 5px 0; padding-left: 20px; color: #616161;">
                        <li>市场格局、用户激活转化、物流履约、风控与补贴策略、支付生态、产品体验观察</li>
                    </ul>
                </li>
                <li style="margin: 10px 0;"><strong>📈 行业与指标分析</strong>
                    <ul style="font-size: 14px; margin: 5px 0; padding-left: 20px; color: #616161;">
                        <li>抖音电商发展历程与竞争格局</li>
                        <li>物流履约核心指标体系与决策树</li>
                        <li>平台/商家/用户多视角数据可视化</li>
                    </ul>
                </li>
                <li style="margin: 10px 0;"><strong>🔬 物流业务AB验证</strong>
                    <ul style="font-size: 14px; margin: 5px 0; padding-left: 20px; color: #616161;">
                        <li>优质快递体验验证：AB测试与因果分析</li>
                        <li>偏远地区物流验证：因果推断与ROI分析</li>
                    </ul>
                </li>
                <li style="margin: 10px 0;"><strong>📊 过往AB测试相关项目</strong>
                    <ul style="font-size: 14px; margin: 5px 0; padding-left: 20px; color: #616161;">
                        <li>MTA归因模型：Shapley Value归因与预算优化AB测试</li>
                    </ul>
                </li>
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
        **v4.0 (2025-10-09 最新版本)** 🎉
        - 🔥 新增双11专题：7个维度深度分析
        - 💰 补贴大战成本控制策略
        - 🤔 产品体验观察与战略思考
        - 💡 总结与讨论：关键思考框架
        - 🎯 新增MTA归因模型AB测试项目
        - 😊 添加"复工快乐"互动彩蛋
        - 📊 大量数据可视化和案例分析
        
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

# ---------------- Page 2: 双11专题 ----------------
elif page == "🔥 双11专题":
    st.header("🛒 双11电商大战：数据洞察与增长策略")
    
    # 顶部提示框
    st.markdown(
        """
        <div style="background-color: #fff3e0; border-left: 5px solid #ff9800; padding: 15px; margin: 15px 0; border-radius: 5px;">
            <h4 style="color: #e65100; margin: 0 0 10px 0;">📅 双11临近，抖音商城已开始预热活动</h4>
            <p style="color: #424242; margin: 5px 0;">
                本专题从<strong>市场格局、用户激活转化、物流履约、风控与补贴策略、支付生态、产品体验观察</strong>等多维度分析抖音如何在双11大战中突围，并提供数据驱动的策略建议。
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Tab 布局
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📊 市场格局", 
        "🎯 用户激活转化", 
        "🚚 双11物流履约",
        "🛡️ 风控与高价值用户", 
        "💳 支付生态布局",
        "🤔 产品体验观察",
        "💡 总结与讨论"
    ])
    
    # ============ Tab 1: 市场格局 ============
    with tab1:
        st.subheader("📈 双11电商平台市场格局演变")
        
        # 双11 GMV数据（基于公开数据和市场研究）
        double11_gmv = pd.DataFrame({
            'year': [2019, 2020, 2021, 2022, 2023, 2024],
            '阿里系（天猫+淘宝）': [2684, 4982, 5403, 5571, 11386, 12500],
            '京东': [2044, 2715, 3491, 3710, 3896, 4200],
            '拼多多': [None, None, None, 520, 780, 1100],
            '抖音电商': [None, None, None, 180, 450, 850],
            '快手电商': [None, None, None, 90, 180, 280],
            '其他平台': [None, None, None, 120, 200, 320]
        })
        
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 12px; border-radius: 8px; margin: 10px 0;">
            <p style="color: #2e7d32; margin: 0;">
                💡 <strong>核心洞察</strong>：抖音电商双11 GMV增速惊人，2023年同比增长150%，2024年同比增长89%
            </p>
            <p style="color: #616161; margin: 5px 0 0 0; font-size: 12px;">
                数据来源：基于公开市场研究报告和各平台财报整理
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 创建GMV趋势图
        gmv_long = double11_gmv.melt(id_vars=['year'], var_name='平台', value_name='GMV')
        gmv_long = gmv_long.dropna()
        
        gmv_chart = alt.Chart(gmv_long).mark_line(
            point=alt.OverlayMarkDef(filled=True, size=80),
            strokeWidth=3
        ).encode(
            x=alt.X('year:O', title='年份', axis=alt.Axis(labelAngle=0)),
            y=alt.Y('GMV:Q', title='GMV (亿元)', scale=alt.Scale(type='log')),
            color=alt.Color('平台:N', 
                          scale=alt.Scale(domain=['阿里系（天猫+淘宝）', '京东', '拼多多', '抖音电商', '快手电商', '其他平台'],
                                        range=['#FF6B6B', '#1976D2', '#FF9933', '#00E5FF', '#FECA57', '#95A5A6'])),
            tooltip=['year:O', '平台:N', alt.Tooltip('GMV:Q', format=',.0f', title='GMV(亿元)')]
        ).properties(
            height=400,
            title=alt.TitleParams(
                text='各平台双11 GMV趋势（2019-2024）',
                fontSize=16,
                fontWeight='bold'
            )
        )
        
        st.altair_chart(gmv_chart, use_container_width=True)
        
        # 2024年市场份额预测
        st.subheader("🎯 2024年双11市场份额")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; padding: 20px; border-radius: 10px; text-align: center;">
                <h3 style="margin: 0; color: white;">64.3%</h3>
                <p style="margin: 5px 0; color: white;">阿里系</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                        color: white; padding: 20px; border-radius: 10px; text-align: center;">
                <h3 style="margin: 0; color: white;">21.6%</h3>
                <p style="margin: 5px 0; color: white;">京东</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                        color: white; padding: 20px; border-radius: 10px; text-align: center;">
                <h3 style="margin: 0; color: white;">4.4%</h3>
                <p style="margin: 5px 0; color: white;">抖音电商 🚀</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **💡 数据驱动的市场策略建议：**
        - 抖音电商市场份额虽小，但增速领先，双11是提升用户心智的关键战役
        - 物流履约能力是决定双11大促成败的核心要素之一
        - 需要在**价格力**、**物流时效**、**用户体验**三者间找到最优平衡
        """)
    
    # ============ Tab 2: 用户增长策略 ============
    with tab2:
        st.subheader("📮 案例：新人红包策略（候选人实际体验")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3;">
                <h4 style="color: #1976d2; margin: 0 0 10px 0;">💰 8元新人红包 + 6天时效</h4>
                <ul style="color: #424242; margin: 10px 0;">
                    <li><strong>目标</strong>：通过时效性刺激快速完成首次转化</li>
                    <li><strong>机制</strong>：过期失效，制造紧迫感</li>
                    <li><strong>配合</strong>：双11红包已在商城显眼位置展示</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # 模拟转化漏斗
            st.markdown("**转化漏斗（模拟数据）**")
            
            funnel_stages = [
                {'name': '新用户注册', 'rate': 100, 'color': '#4CAF50', 'width': 100},
                {'name': '领取红包', 'rate': 85, 'color': '#8BC34A', 'width': 85},
                {'name': '浏览商品', 'rate': 73, 'color': '#FFC107', 'width': 73},
                {'name': '加购', 'rate': 61, 'color': '#FF9800', 'width': 61},
                {'name': '下单支付', 'rate': 55, 'color': '#F44336', 'width': 55}
            ]
            
            for stage in funnel_stages:
                st.markdown(f"""
                <div style="margin: 8px 0;">
                    <div style="background: linear-gradient(to right, {stage['color']} {stage['width']}%, #f5f5f5 {stage['width']}%);
                                padding: 10px;
                                border-radius: 5px;
                                border-left: 4px solid {stage['color']};
                                display: flex;
                                justify-content: space-between;
                                align-items: center;">
                        <span style="font-size: 13px; color: #424242; font-weight: 500;">{stage['name']}</span>
                        <span style="font-size: 16px; color: {stage['color']}; font-weight: bold;">{stage['rate']}%</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # AB测试建议
        st.markdown("""
        ---
        ### 🔬 建议开展的AB测试
        """)
        
        ab_test_df = pd.DataFrame({
            '测试维度': ['红包面额', '时效设置', '发放时机'],
            '对照组': ['8元/6天', '6天有效期', '注册后即发'],
            '实验组': ['12元/3天', '3天有效期', '首次浏览商品后发'],
            '核心指标': ['首单转化率', '下单紧迫性', '浏览深度→转化'],
            '预期提升': ['+15%', '+22%', '+18%']
        })
        
        st.dataframe(ab_test_df, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <p style="color: #616161; margin: 10px 0; font-size: 12px;">
            注：物流相关AB测试详见"双11物流履约"专题
        </p>
        """, unsafe_allow_html=True)
    
    # ============ Tab 3: 双11物流履约 ============
    with tab3:
        st.subheader("🚚 双11物流履约：大促期间的物流挑战与策略")
        
        # 顶部说明
        st.markdown("""
        <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3; margin-bottom: 20px;">
            <p style="color: #1565c0; margin: 0; font-size: 15px;">
                双11期间订单量激增，物流履约能力直接影响用户体验和复购率。本专题分析物流挑战、解决方案及关键指标。
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 双11物流挑战
        st.markdown("### 📦 双11物流三大核心挑战")
        
        challenge_cols = st.columns(3)
        
        with challenge_cols[0]:
            st.markdown("""
            <div style="background-color: #ffebee; padding: 20px; border-radius: 10px; height: 240px;">
                <h4 style="color: #c62828; margin: 0 0 15px 0;">⚡ 订单量激增</h4>
                <ul style="font-size: 14px; color: #424242; line-height: 1.8;">
                    <li>日均订单量增长<strong>8-15倍</strong></li>
                    <li>0-2点订单峰值占比<strong>35%+</strong></li>
                    <li>履约时效压力骤增</li>
                    <li>仓储爆仓风险</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with challenge_cols[1]:
            st.markdown("""
            <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; height: 240px;">
                <h4 style="color: #e65100; margin: 0 0 15px 0;">🎯 时效承诺压力</h4>
                <ul style="font-size: 14px; color: #424242; line-height: 1.8;">
                    <li>用户期待<strong>次日达/当日达</strong></li>
                    <li>小时达订单占比提升</li>
                    <li>延迟赔付成本上升</li>
                    <li>客诉率敏感期</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with challenge_cols[2]:
            st.markdown("""
            <div style="background-color: #f3e5f5; padding: 20px; border-radius: 10px; height: 240px;">
                <h4 style="color: #7b1fa2; margin: 0 0 15px 0;">💰 成本控制难题</h4>
                <ul style="font-size: 14px; color: #424242; line-height: 1.8;">
                    <li>快递费用临时上涨<strong>20-30%</strong></li>
                    <li>加班人力成本</li>
                    <li>包邮策略侵蚀利润</li>
                    <li>退换货物流成本</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # 物流数据分析
        st.markdown("---")
        st.markdown("### 📊 双11物流关键指标对比（平日 vs 双11）")
        
        logistics_metrics = pd.DataFrame({
            '指标': ['日均订单量', '准时达率', '平均配送时长', '客诉率', '单件物流成本', '退货率'],
            '平日基线': ['100万', '92%', '48小时', '0.8%', '6.5元', '5%'],
            '双11峰值': ['1200万', '78%', '72小时', '3.2%', '8.5元', '8%'],
            '变化幅度': ['+1100%', '-15%', '+50%', '+300%', '+31%', '+60%'],
            '目标值': ['1200万', '≥85%', '≤60小时', '≤2%', '≤7.5元', '≤6.5%']
        })
        
        st.dataframe(logistics_metrics, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <p style="color: #616161; margin: 10px 0; font-size: 12px;">
            数据来源：基于抖音电商物流公开数据及行业研究报告（模拟数据）
        </p>
        """, unsafe_allow_html=True)
        
        # 解决方案
        st.markdown("---")
        st.markdown("### 🎯 数据驱动的物流优化策略")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 📍 策略一：智能快递商分配
            
            <div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
                <p style="color: #2e7d32; font-weight: bold; margin: 0 0 10px 0;">核心逻辑</p>
                <ul style="color: #424242; font-size: 14px; margin: 0;">
                    <li>基于历史数据建立快递商<strong>时效评分模型</strong></li>
                    <li>实时监测各快递商双11履约表现</li>
                    <li>动态调整订单分配权重</li>
                    <li>优先分配表现优异的快递商</li>
                </ul>
            </div>
            
            <div style="background-color: #fff3e0; padding: 12px; border-radius: 8px; margin-top: 15px;">
                <p style="color: #e65100; font-weight: bold; margin: 0 0 8px 0;">📈 预期效果</p>
                <ul style="color: #424242; font-size: 13px; margin: 0;">
                    <li>准时达率提升 <strong>7-10个百分点</strong></li>
                    <li>客诉率降低 <strong>25%</strong></li>
                    <li>用户NPS提升 <strong>8分</strong></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            #### 🏪 策略二：前置仓+预测性备货
            
            <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3;">
                <p style="color: #1565c0; font-weight: bold; margin: 0 0 10px 0;">核心逻辑</p>
                <ul style="color: #424242; font-size: 14px; margin: 0;">
                    <li>基于用户浏览/加购数据<strong>预测爆款</strong></li>
                    <li>提前将热销商品下沉到前置仓</li>
                    <li>核心城市实现<strong>2小时达</strong></li>
                    <li>减少主仓发货压力</li>
                </ul>
            </div>
            
            <div style="background-color: #f3e5f5; padding: 12px; border-radius: 8px; margin-top: 15px;">
                <p style="color: #7b1fa2; font-weight: bold; margin: 0 0 8px 0;">📈 预期效果</p>
                <ul style="color: #424242; font-size: 13px; margin: 0;">
                    <li>小时达订单占比提升至 <strong>18%</strong></li>
                    <li>平均配送时长缩短 <strong>12小时</strong></li>
                    <li>复购率提升 <strong>15%</strong></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # AB测试设计
        st.markdown("---")
        st.markdown("### 🔬 物流体验优化AB测试")
        
        logistics_ab_test = pd.DataFrame({
            '测试维度': ['快递商展示', '物流承诺', '配送提醒频次', '包装升级'],
            '对照组': [
                '默认快递（价格优先）',
                '预计3-5天送达',
                '发货+签收通知',
                '标准包装'
            ],
            '实验组': [
                '优质快递+时效标识',
                '承诺48小时达+延迟赔付',
                '发货+运输中+派件+签收',
                '环保+防摔包装'
            ],
            '核心指标': [
                '选择率、NPS、复购率',
                '下单转化率、投诉率',
                '用户满意度、查询次数',
                '好评率、退货率'
            ],
            '预期提升': ['+20%', '+12%', '+8%', '+15%']
        })
        
        st.dataframe(logistics_ab_test, use_container_width=True, hide_index=True)
        
        # 监控看板
        st.markdown("---")
        st.markdown("### 📺 双11物流实时监控看板（示意）")
        
        monitor_cols = st.columns(4)
        
        with monitor_cols[0]:
            st.metric(
                label="当前待发货订单",
                value="328万",
                delta="+15%",
                delta_color="inverse"
            )
        
        with monitor_cols[1]:
            st.metric(
                label="实时准时达率",
                value="82.3%",
                delta="-3.2%",
                delta_color="inverse"
            )
        
        with monitor_cols[2]:
            st.metric(
                label="今日客诉率",
                value="2.1%",
                delta="+0.3%",
                delta_color="inverse"
            )
        
        with monitor_cols[3]:
            st.metric(
                label="小时达订单占比",
                value="14.8%",
                delta="+2.5%",
                delta_color="normal"
            )
        
        st.markdown("""
        <div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-top: 15px; border-left: 4px solid #ff9800;">
            <h4 style="color: #e65100; margin: 0 0 10px 0;">💡 关键洞察</h4>
            <ul style="color: #424242; margin: 0;">
                <li><strong>物流体验是用户复购的核心驱动因素</strong>：准时达率每提升1%，次月复购率提升0.8%</li>
                <li><strong>小时达是差异化竞争优势</strong>：使用过小时达的用户，LTV是普通用户的2.3倍</li>
                <li><strong>智能分配可平衡成本和体验</strong>：通过算法优化，在不增加成本的前提下提升10%时效</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # ============ Tab 4: 风控与高价值用户 ============
    with tab4:
        st.subheader("🛡️ 防薅羊毛 & 高价值用户识别")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### ⚠️ 薅羊毛用户特征识别
            
            <div style="background-color: #ffebee; padding: 15px; border-radius: 8px; border-left: 4px solid #f44336;">
                <h4 style="color: #c62828; margin-top: 0;">🚨 高风险行为模式</h4>
                <ul style="color: #424242;">
                    <li>注册后仅领券不浏览</li>
                    <li>只购买红包覆盖的低价商品</li>
                    <li>从不互动（点赞/评论/分享）</li>
                    <li>多账号关联（设备/地址）</li>
                    <li>高退货率（>50%）</li>
                    <li>客单价长期低于红包面额</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **🔧 数据模型建议：**
            - **特征工程**：用户行为序列、时间窗口内的订单模式、社交互动指数
            - **模型选择**：XGBoost / LightGBM（可解释性+准确率）
            - **标签定义**：30天内LTV < 红包总额 = 羊毛党候选
            """)
        
        with col2:
            st.markdown("""
            ### 💎 高价值用户画像
            
            <div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
                <h4 style="color: #2e7d32; margin-top: 0;">⭐ 核心特征</h4>
                <ul style="color: #424242;">
                    <li>月均下单频次 > 3次</li>
                    <li>客单价 > 平台均值1.5倍</li>
                    <li>跨品类购买（3+品类）</li>
                    <li>观看直播时长 > 30分钟/周</li>
                    <li>主动分享/种草行为</li>
                    <li>低退货率（<5%）</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **💰 LTV预估模型：**
            - **RFM模型**：Recency, Frequency, Monetary
            - **生命周期预测**：基于Survival Analysis
            - **推荐策略**：高价值用户定向push高客单价商品
            """)
        
        # 用户分层可视化
        st.markdown("---")
        st.markdown("### 📊 用户价值分层（RFM模型示例）")
        
        # 模拟RFM分层数据
        rfm_data = pd.DataFrame({
            '用户分层': ['超级用户', '高价值用户', '潜力用户', '一般用户', '流失预警', '羊毛党'],
            '占比': [5, 15, 25, 35, 15, 5],
            'LTV（元）': [5800, 2200, 800, 350, 120, 15],
            '月均订单': [8.5, 4.2, 2.1, 1.2, 0.3, 0.8],
            '双11策略': [
                '专属客服+会员特权+提前购',
                '大额券+品类推荐+邮费全免',
                '品类券+社交裂变+新人推荐奖励',
                '通用券+爆款推荐',
                '召回红包+个性化推送',
                '限制红包发放+风控监测'
            ]
        })
        
        st.dataframe(rfm_data, use_container_width=True, hide_index=True)
        
        # 策略建议
        st.markdown("""
        <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; margin-top: 15px;">
            <h4 style="color: #1976d2; margin-top: 0;">💡 双11风控策略建议</h4>
            <ol style="color: #424242;">
                <li><strong>预算分配</strong>：70%预算给高价值+潜力用户，20%给一般用户，10%用于拉新</li>
                <li><strong>实时监控</strong>：建立羊毛党行为实时监测看板，异常账号自动限流</li>
                <li><strong>物流关联</strong>：同地址/收件人批量订单触发人工审核</li>
                <li><strong>动态调整</strong>：根据活动进展动态调整红包发放策略</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # 补贴大战与成本控制
        st.markdown("---")
        st.markdown("### 💰 补贴大战：如何避免无底洞式烧钱？")
        
        # 问题背景
        st.markdown("""
        <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; border-left: 5px solid #ff9800; margin-bottom: 20px;">
            <h4 style="color: #e65100; margin: 0 0 12px 0;">🔥 当前补贴大战现状</h4>
            <p style="color: #424242; margin: 0 0 10px 0; line-height: 1.8;">
                各大电商平台（包括外卖、即时零售）正在进行新一轮补贴大战，疯狂发放红包券。但<strong>无序补贴</strong>会导致：
            </p>
            <ul style="color: #424242; margin: 0;">
                <li>💸 补贴成本失控，烧钱无底洞</li>
                <li>🎭 大量羊毛党涌入，补贴被薅走</li>
                <li>📉 停止补贴后用户大量流失，无忠诚度</li>
                <li>⚖️ 行业陷入恶性竞争，整体利润率下降</li>
                <li>🏢 中小平台难以承受，市场垄断加剧</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 案例分析 - 移到这里
        st.markdown("### 📚 案例分析：补贴策略的成败")
        
        case_df = pd.DataFrame({
            '平台': ['滴滴（早期）', '拼多多', '瑞幸咖啡', '淘特（失败案例）'],
            '补贴策略': [
                '司机+乘客双向补贴，快速占领市场',
                '社交裂变+低价补贴，下沉市场突破',
                '首杯免费+持续优惠券，培养咖啡习惯',
                '无差别大额补贴，未做用户筛选'
            ],
            '数据表现': [
                '6个月用户增长1000%，但补贴成本高达70%',
                '用户留存率42%，LTV/CAC=3.5（健康）',
                '复购率从15%提升到45%，逐步减少补贴',
                '获客成本>LTV，大量羊毛党，补贴停止后流失率85%'
            ],
            '结果': [
                '✅ 成功占领市场，后期提价盈利',
                '✅ 建立用户心智，补贴效率高',
                '✅ 培养消费习惯，实现自然增长',
                '❌ 亏损严重，业务收缩'
            ]
        })
        
        st.dataframe(case_df, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <p style="color: #616161; margin: 10px 0; font-size: 12px;">
            💡 核心启示：补贴不是目的，而是获取高质量用户的手段。精准补贴 > 全面补贴。
        </p>
        """, unsafe_allow_html=True)
        
        # 数据驱动的成本控制策略
        st.markdown("### 📊 数据驱动的补贴成本控制策略")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; min-height: 380px;">
                <h4 style="color: #2e7d32; margin: 0 0 15px 0;">✅ 核心原则</h4>
                <ol style="color: #424242; font-size: 14px; line-height: 1.8;">
                    <li><strong>精准补贴 > 普惠补贴</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>基于用户LTV预测模型分层补贴</li>
                            <li>高潜力用户：大额券</li>
                            <li>一般用户：中额券</li>
                            <li>羊毛党：限制或不发</li>
                        </ul>
                    </li>
                    <li><strong>ROI阈值控制</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>设定最低ROI目标（如1:3）</li>
                            <li>补贴1元需带来3元GMV</li>
                            <li>实时监控，动态调整</li>
                        </ul>
                    </li>
                    <li><strong>渐进式补贴</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>首单：大额补贴吸引</li>
                            <li>2-5单：中额补贴培养习惯</li>
                            <li>6单+：小额补贴或取消</li>
                        </ul>
                    </li>
                    <li><strong>行为触发 > 无条件发放</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>浏览N分钟后发券</li>
                            <li>加购未下单时发券</li>
                            <li>流失召回时发券</li>
                        </ul>
                    </li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; min-height: 380px;">
                <h4 style="color: #1565c0; margin: 0 0 15px 0;">📈 数据监测指标体系</h4>
                <ol style="color: #424242; font-size: 14px; line-height: 1.8;">
                    <li><strong>成本效率指标</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>CAC（获客成本）</li>
                            <li>补贴ROI = GMV / 补贴成本</li>
                            <li>人均补贴金额</li>
                        </ul>
                    </li>
                    <li><strong>用户质量指标</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>补贴用户vs自然用户留存率对比</li>
                            <li>补贴停止后的留存率</li>
                            <li>30天LTV / CAC 比值</li>
                        </ul>
                    </li>
                    <li><strong>风险预警指标</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>羊毛党占比（>5%预警）</li>
                            <li>补贴依赖度（补贴订单占比>70%危险）</li>
                            <li>补贴成本占GMV比例（>15%需优化）</li>
                        </ul>
                    </li>
                    <li><strong>竞争情报指标</strong>
                        <ul style="font-size: 13px; margin: 5px 0;">
                            <li>竞品补贴力度监测</li>
                            <li>市场份额变化</li>
                            <li>用户流失去向分析</li>
                        </ul>
                    </li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        # 如何回归良性竞争
        st.markdown("---")
        st.markdown("### 🤝 如何从补贴大战回归良性竞争？")
        
        st.markdown("""
        <div style="background-color: #f3e5f5; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h4 style="color: #7b1fa2; margin: 0 0 15px 0;">🎯 长期策略：从价格战到价值战</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0;">
                    <h5 style="color: #7b1fa2; margin: 0 0 10px 0;">1️⃣ 差异化竞争</h5>
                    <ul style="font-size: 14px; color: #424242; margin: 0;">
                        <li><strong>淘宝/天猫</strong>：商品丰富度+生态完整性</li>
                        <li><strong>京东</strong>：自营品质+物流时效</li>
                        <li><strong>拼多多</strong>：社交裂变+下沉市场</li>
                        <li><strong>抖音</strong>：内容+电商（直播带货）</li>
                    </ul>
                    <p style="font-size: 13px; color: #616161; margin: 10px 0 0 0;">
                        💡 <strong>核心</strong>：找到自己的护城河，不打价格战
                    </p>
                </div>
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0;">
                    <h5 style="color: #7b1fa2; margin: 0 0 10px 0;">2️⃣ 用户体验为王</h5>
                    <ul style="font-size: 14px; color: #424242; margin: 0;">
                        <li>物流时效</li>
                        <li>商品品质</li>
                        <li>售后服务</li>
                        <li>APP性能</li>
                    </ul>
                    <p style="font-size: 13px; color: #616161; margin: 10px 0 0 0;">
                        💡 <strong>核心</strong>：好的体验比便宜更有粘性
                    </p>
                </div>
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0;">
                    <h5 style="color: #7b1fa2; margin: 0 0 10px 0;">3️⃣ 会员体系替代补贴</h5>
                    <ul style="font-size: 14px; color: #424242; margin: 0;">
                        <li>年费会员享受长期优惠</li>
                        <li>提前锁定用户</li>
                        <li>降低营销成本</li>
                        <li>提升用户忠诚度</li>
                    </ul>
                    <p style="font-size: 13px; color: #616161; margin: 10px 0 0 0;">
                        💡 <strong>核心</strong>：从一次性补贴到长期价值绑定
                    </p>
                </div>
                <div style="background-color: white; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0;">
                    <h5 style="color: #7b1fa2; margin: 0 0 10px 0;">4️⃣ 数据驱动的精准运营</h5>
                    <ul style="font-size: 14px; color: #424242; margin: 0;">
                        <li>千人千面的个性化推荐</li>
                        <li>基于LTV的用户分层</li>
                        <li>智能定价</li>
                        <li>预测性补货</li>
                    </ul>
                    <p style="font-size: 13px; color: #616161; margin: 10px 0 0 0;">
                        💡 <strong>核心</strong>：用技术和数据提升效率
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # ============ Tab 5: 支付生态布局 ============
    with tab5:
        st.subheader("💳 抖音支付：支付市场的战略布局")
        
        # 顶部洞察
        st.markdown("""
        <div style="background-color: #fce4ec; padding: 20px; border-radius: 10px; border-left: 5px solid #e91e63; margin-bottom: 20px;">
            <h4 style="color: #c2185b; margin: 0 0 10px 0;">🔍 实际观察</h4>
            <ul style="color: #424242; margin: 0;">
                <li>新人开通抖音支付并关联银行卡赠送 <strong>15.88元现金奖励</strong>，快速到账</li>
                <li>苹果账户支付选项中新增 <strong>抖音支付</strong>（此前仅有微信、支付宝）</li>
                <li>这是抖音支付抢占中国线上支付市场的重要信号</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 支付市场格局
        st.markdown("### 📊 中国移动支付市场格局（2024）")
        
        payment_share = pd.DataFrame({
            '支付方式': ['支付宝', '微信支付', '银联云闪付', '抖音支付', '其他'],
            '市场份额(%)': [54.2, 38.6, 4.8, 1.2, 1.2],
            '用户规模(亿)': [10.5, 9.2, 3.8, 0.8, 0.5]
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            # 市场份额饼图
            payment_chart = alt.Chart(payment_share).mark_arc(innerRadius=60).encode(
                theta=alt.Theta('市场份额(%):Q'),
                color=alt.Color('支付方式:N', 
                              scale=alt.Scale(range=['#1677ff', '#52c41a', '#fa8c16', '#eb2f96', '#95a5a6'])),
                tooltip=['支付方式', '市场份额(%)', '用户规模(亿)']
            ).properties(
                height=300,
                title='移动支付市场份额'
            )
            st.altair_chart(payment_chart, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div style="background-color: #f0f5ff; padding: 20px; border-radius: 8px; height: 300px; display: flex; flex-direction: column; justify-content: center;">
                <h4 style="color: #1677ff; margin: 0 0 15px 0;">📈 抖音支付增长潜力</h4>
                <div style="margin-bottom: 15px;">
                    <p style="margin: 5px 0; color: #424242;"><strong>月活用户：</strong>10.2亿+ <a href="https://m.ebrun.com/ebrungo/zb/586280.html" target="_blank" style="font-size: 11px; color: #1677ff;">[来源]</a></p>
                    <p style="margin: 5px 0; color: #424242;"><strong>日均支付场景：</strong>电商/生活服务/充值</p>
                    <p style="margin: 5px 0; color: #424242;"><strong>差异化优势：</strong>内容+交易闭环</p>
                </div>
                <div style="background-color: #e6f7ff; padding: 10px; border-radius: 5px; border-left: 3px solid #1677ff;">
                    <p style="margin: 0; color: #0050b3; font-size: 14px;">
                        💡 
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <p style="color: #616161; margin: 10px 0; font-size: 12px;">
            数据来源：抖音月活数据来自电商报（2025年5月），GMV目标来自公开市场研究报告
        </p>
        """, unsafe_allow_html=True)
        
        # 战略分析
        st.markdown("---")
        st.markdown("### 🎯 抖音支付的战略意义")
        
        strategy_cols = st.columns(3)
        
        with strategy_cols[0]:
            st.markdown("""
            <div style="background-color: #e6f7ff; padding: 15px; border-radius: 8px; height: 280px;">
                <h4 style="color: #0050b3;">💰 经济价值</h4>
                <ul style="font-size: 14px; color: #424242;">
                    <li><strong>支付规模</strong>：若抖音支付在电商场景渗透率达50%，可贡献年GMV 2.1万亿+的支付规模（基于2025年GMV目标4.2万亿）</li>
                    <li><strong>手续费收入</strong>：按0.1%费率和50%渗透率估算，2025年GMV目标4.2万亿可带来21亿元</li>
                    <li><strong>资金沉淀</strong>：零钱余额产生利息收入</li>
                    <li><strong>金融延展</strong>：消费信贷、理财等</li>
                </ul>
                <p style="font-size: 11px; color: #616161; margin-top: 10px;">注：费率为行业通用估算</p>
            </div>
            """, unsafe_allow_html=True)
        
        with strategy_cols[1]:
            st.markdown("""
            <div style="background-color: #f6ffed; padding: 15px; border-radius: 8px; height: 280px;">
                <h4 style="color: #389e0d;">🔒 数据价值</h4>
                <ul style="font-size: 14px; color: #424242;">
                    <li><strong>完整交易链路</strong>：从浏览到支付全掌握</li>
                    <li><strong>用户画像增强</strong>：消费能力精准评估</li>
                    <li><strong>风控能力</strong>：识别异常交易和欺诈</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with strategy_cols[2]:
            st.markdown("""
            <div style="background-color: #fff7e6; padding: 15px; border-radius: 8px; height: 280px;">
                <h4 style="color: #d46b08;">🚀 生态价值</h4>
                <ul style="font-size: 14px; color: #424242;">
                    <li><strong>降低依赖</strong>：减少对微信/支付宝的依赖</li>
                    <li><strong>用户粘性</strong>：支付绑定提升留存</li>
                    <li><strong>场景拓展</strong>：线下支付、跨境支付</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # 双11期间的支付策略
        st.markdown("---")
        st.markdown("### 🔥 双11期间抖音支付推广策略建议")
        
        st.markdown("""
        <div style="background-color: #fff0f6; padding: 20px; border-radius: 10px; border-left: 5px solid #eb2f96;">
            <h4 style="color: #c41d7f; margin-top: 0;">💎 激励策略</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">
                <div style="background-color: white; padding: 12px; border-radius: 6px;">
                    <strong style="color: #eb2f96;">🎁 首次绑卡奖励</strong>
                    <p style="margin: 5px 0 0 0; font-size: 14px; color: #424242;">
                        绑定银行卡送20-30元券包
                    </p>
                </div>
                <div style="background-color: white; padding: 12px; border-radius: 6px;">
                    <strong style="color: #eb2f96;">💰 支付立减</strong>
                    <p style="margin: 5px 0 0 0; font-size: 14px; color: #424242;">
                        使用抖音支付享受随机立减
                    </p>
                </div>
                <div style="background-color: white; padding: 12px; border-radius: 6px;">
                    <strong style="color: #eb2f96;">🎲 支付抽奖</strong>
                    <p style="margin: 5px 0 0 0; font-size: 14px; color: #424242;">
                        每笔支付参与抽奖（最高免单）
                    </p>
                </div>
                <div style="background-color: white; padding: 12px; border-radius: 6px;">
                    <strong style="color: #eb2f96;">⚡ 时段加码</strong>
                    <p style="margin: 5px 0 0 0; font-size: 14px; color: #424242;">
                        0-2点使用抖音支付额外返现
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 数据监测指标
        st.markdown("---")
        st.markdown("### 📈 关键监测指标")
        
        metrics_df = pd.DataFrame({
            '指标类别': ['渗透率', '活跃度', '留存', '交易规模'],
            '核心指标': [
                '抖音支付使用率',
                '人均支付笔数',
                '次月支付留存率',
                '支付GMV占比'
            ],
            '双11目标': ['35%', '2.5笔', '65%', '25%'],
            '当前基线': ['18%', '1.2笔', '48%', '12%'],
            '提升空间': ['+94%', '+108%', '+35%', '+108%']
        })
        
        st.dataframe(metrics_df, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <p style="color: #616161; margin: 10px 0; font-size: 12px;">
            注：监测指标目标值基于行业基准和历史数据模拟
        </p>
        """, unsafe_allow_html=True)
    
    # ============ Tab 6: 产品体验观察 ============
    with tab6:
        st.subheader("🤔 产品体验观察与战略思考")
        
        # 顶部说明
        st.markdown("""
        <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3; margin-bottom: 20px;">
            <p style="color: #1565c0; margin: 0; font-size: 15px;">
                基于候选人实际使用抖音APP的体验观察，从数据与产品角度提出思考和建议。
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 观察1: APP性能问题
        st.markdown("### ⚡ 观察一：APP性能体验待优化")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            <div style="background-color: #ffebee; padding: 20px; border-radius: 10px; border-left: 5px solid #f44336;">
                <h4 style="color: #c62828; margin: 0 0 12px 0;">🐌 问题描述</h4>
                <p style="color: #424242; margin: 0 0 10px 0;">
                    实际使用中发现抖音APP存在卡顿现象，特别是在商城浏览、切换Tab、加载商品详情时表现明显。
                </p>
                <p style="color: #616161; font-size: 14px; margin: 0;">
                    <strong>影响：</strong>影响用户体验，可能导致流失和转化率下降
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; margin-top: 15px; border-left: 4px solid #4caf50;">
                <h4 style="color: #2e7d32; margin: 0 0 10px 0;">📊 数据监测建议</h4>
                <ul style="color: #424242; font-size: 14px; margin: 0;">
                    <li><strong>性能指标</strong>：页面加载时间、FPS、内存占用、崩溃率</li>
                    <li><strong>用户行为</strong>：卡顿发生时的用户流失率、返回率</li>
                    <li><strong>设备分析</strong>：按机型、系统版本、网络状况分层监测</li>
                    <li><strong>AB测试</strong>：性能优化版 vs 当前版，观察对转化率的影响</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; height: 480px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h4 style="color: #e65100; margin: 0 0 15px 0;">💡 优化方向</h4>
                    <ol style="color: #424242; font-size: 14px; line-height: 1.8;">
                        <li><strong>代码层面</strong>：
                            <ul style="font-size: 13px; margin: 5px 0;">
                                <li>资源懒加载</li>
                                <li>图片压缩优化</li>
                                <li>减少渲染层级</li>
                            </ul>
                        </li>
                        <li><strong>架构层面</strong>：
                            <ul style="font-size: 13px; margin: 5px 0;">
                                <li>CDN加速</li>
                                <li>预加载策略</li>
                                <li>缓存机制</li>
                            </ul>
                        </li>
                        <li><strong>数据层面</strong>：
                            <ul style="font-size: 13px; margin: 5px 0;">
                                <li>建立性能监控看板</li>
                                <li>识别高频卡顿场景</li>
                                <li>量化优化效果</li>
                            </ul>
                        </li>
                    </ol>
                </div>
                <div style="background-color: #fbe9e7; padding: 10px; border-radius: 5px; margin-top: 10px;">
                    <p style="margin: 0; font-size: 13px; color: #bf360c;">
                        <strong>核心观点：</strong>性能不仅是技术问题，更是商业问题。页面加载时间每增加1秒，转化率可能下降7%
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # 观察2: 超级APP战略
        st.markdown("---")
        st.markdown("### 🌐 观察二：超级APP现象的战略思考")
        
        st.markdown("""
        <div style="background-color: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 5px solid #9c27b0; margin-bottom: 20px;">
            <h4 style="color: #7b1fa2; margin: 0 0 12px 0;">🤔 现象观察</h4>
            <p style="color: #424242; margin: 0; line-height: 1.8;">
                国内APP（抖音、微信、支付宝、美团等）都在向超级APP演进，试图一网打尽所有消费场景。
                抖音从短视频起家，现已涵盖：电商、支付、外卖、酒旅、本地生活、团购等。
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 利弊分析
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; min-height: 320px;">
                <h4 style="color: #2e7d32; margin: 0 0 15px 0;">✅ 优势（数据视角）</h4>
                <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                    <li><strong>数据闭环</strong>：用户行为数据全链路打通，从浏览、社交到消费、支付</li>
                    <li><strong>用户画像增强</strong>：多场景数据交叉验证，精准度提升</li>
                    <li><strong>交叉销售</strong>：基于数据的场景推荐（看直播→电商→外卖）</li>
                    <li><strong>用户粘性</strong>：多场景满足，降低卸载率，提升DAU</li>
                    <li><strong>LTV提升</strong>：单用户贡献多个场景的价值</li>
                    <li><strong>网络效应</strong>：场景越多，数据越丰富，算法越精准</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background-color: #ffebee; padding: 20px; border-radius: 10px; min-height: 320px;">
                <h4 style="color: #c62828; margin: 0 0 15px 0;">⚠️ 挑战（数据视角）</h4>
                <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                    <li><strong>性能问题</strong>：功能臃肿导致APP卡顿，负面体验数据上升</li>
                    <li><strong>用户认知混乱</strong>：品牌定位模糊，用户不知"这个APP是干什么的"</li>
                    <li><strong>核心业务稀释</strong>：资源分散，可能导致主营业务数据下滑</li>
                    <li><strong>监管风险</strong>：数据垄断、隐私保护、不正当竞争</li>
                    <li><strong>运营复杂度</strong>：多业务线数据指标体系庞杂，难以聚焦</li>
                    <li><strong>用户疲劳</strong>：功能过载，关键功能埋藏太深，降低使用频率</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # 数据驱动的战略建议
        st.markdown("""
        <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; margin-top: 20px; border-left: 5px solid #2196f3;">
            <h4 style="color: #1565c0; margin: 0 0 15px 0;">📊 数据驱动的战略建议</h4>
            <ol style="color: #424242; font-size: 15px; line-height: 2;">
                <li><strong>场景协同而非简单堆砌</strong>：用数据验证场景间的协同效应（如直播→电商转化率>30%才有价值）</li>
                <li><strong>建立优先级矩阵</strong>：基于用户使用频率、贡献GMV、数据价值评估每个场景的ROI</li>
                <li><strong>差异化定位</strong>：抖音的优势在"内容+交易"，不是所有场景都适合做（如金融、医疗等重决策场景）</li>
                <li><strong>性能为王</strong>：持续监测APP性能指标，确保在功能扩展的同时不损害核心体验</li>
                <li><strong>用户分层运营</strong>：不同用户群体对超级APP的接受度不同，需要数据分析+精准触达</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # 观察3: 用户反馈功能
        st.markdown("---")
        st.markdown("### 📢 观察三：用户反馈机制待改进")
        
        st.markdown("""
        <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; border-left: 5px solid #ff9800;">
            <h4 style="color: #e65100; margin: 0 0 12px 0;">🔍 问题发现</h4>
            <p style="color: #424242; margin: 0 0 10px 0; font-size: 14px;">
                长按反馈问题功能体验不佳：长按后没有反应
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # ============ Tab 7: 总结与讨论 ============
    with tab7:
        # 关键思考框架 - 置顶
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 25px; border-radius: 15px; margin-bottom: 30px;">
            <h3 style="color: white; margin: 0 0 18px 0;">🎯 关键思考框架</h3>
            <ol style="color: white; font-size: 15px; line-height: 2;">
                <li><strong>增长飞轮</strong>：红包激励 → 首次下单 → 优质物流体验 → 支付绑定 → 复购提升 → LTV增长 → 高价值用户沉淀</li>
                <li><strong>数据驱动</strong>：所有策略均基于数据分析和AB测试验证，避免拍脑袋决策</li>
                <li><strong>全局视角</strong>：从市场格局、用户增长、物流履约、风控、支付生态等多维度构建完整的业务理解</li>
                <li><strong>体验至上</strong>：物流、支付等"基础设施"不是成本，而是用户体验和差异化竞争的核心</li>
                <li><strong>风险平衡</strong>：在追求GMV增长的同时，必须严控薅羊毛行为，确保ROI健康和可持续增长</li>
                <li><strong>生态思维</strong>：电商+物流+支付形成闭环，数据互通，协同增效</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Tab1: 市场格局讨论要点
        st.markdown("### 📊 市场格局分析要点")
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 18px; border-radius: 8px; margin-bottom: 20px;">
            <h4 style="color: #1976d2; margin: 0 0 12px 0;">核心观点</h4>
            <ul style="color: #424242; line-height: 1.8;">
                <li><strong>市场机会</strong>：抖音电商正处于快速增长期（2024年双11 GMV增长89%），双11是提升用户心智和市场份额的关键战役</li>
                <li><strong>竞争格局</strong>：阿里系份额下降但仍占主导（64.3%），拼多多和抖音是增长最快的挑战者</li>
                <li><strong>数据驱动洞察</strong>：通过历史GMV趋势预测市场格局变化，为战略决策提供数据支撑</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Tab2: 用户激活转化讨论要点
        st.markdown("### 🎯 用户激活转化讨论要点")
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 18px; border-radius: 8px; margin-bottom: 20px;">
            <h4 style="color: #1976d2; margin: 0 0 12px 0;">核心观点</h4>
            <ul style="color: #424242; line-height: 1.8;">
                <li><strong>红包策略</strong>：8元红包+6天时效的设计利用时间紧迫感促进首次转化，结合实际用户体验分析产品设计</li>
                <li><strong>转化漏斗</strong>：从注册到支付的多阶段转化漏斗，识别关键流失点并优化</li>
                <li><strong>AB测试设计</strong>：针对红包面额、时效设置、发放时机等维度设计实验，预期提升15-22%</li>
                <li><strong>数据方法论</strong>：通过AB测试验证产品假设，用数据驱动决策而非主观判断</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Tab3: 双11物流履约讨论要点
        st.markdown("### 🚚 双11物流履约讨论要点")
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 18px; border-radius: 8px; margin-bottom: 20px;">
            <h4 style="color: #1976d2; margin: 0 0 12px 0;">核心观点</h4>
            <ul style="color: #424242; line-height: 1.8;">
                <li><strong>三大挑战</strong>：订单量激增（8-15倍）、时效承诺压力、成本控制难题</li>
                <li><strong>智能分配策略</strong>：基于历史数据建立快递商评分模型，动态优化订单分配，可提升准时达率7-10个百分点</li>
                <li><strong>前置仓布局</strong>：通过预测性备货实现小时达，差异化竞争优势明显（小时达用户LTV是普通用户2.3倍）</li>
                <li><strong>数据与体验</strong>：物流履约不仅是成本中心，更是用户体验和复购率的核心驱动因素（准时达率每提升1%，次月复购率提升0.8%）</li>
                <li><strong>AB测试场景</strong>：快递商展示、物流承诺、配送提醒、包装升级等维度均可开展实验</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Tab4: 风控与高价值用户讨论要点
        st.markdown("### 🛡️ 风控与补贴策略讨论要点")
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 18px; border-radius: 8px; margin-bottom: 20px;">
            <h4 style="color: #1976d2; margin: 0 0 12px 0;">核心观点</h4>
            <ul style="color: #424242; line-height: 1.8;">
                <li><strong>风险识别</strong>：通过行为特征（领券不浏览、低价商品、高退货率等）识别薅羊毛用户</li>
                <li><strong>数据模型</strong>：使用XGBoost/LightGBM构建风控模型，特征工程包括用户行为序列、订单模式、社交互动等</li>
                <li><strong>用户分层</strong>：基于RFM模型将用户分为6层（超级用户、高价值、潜力、一般、流失预警、羊毛党），针对性运营</li>
                <li><strong>预算分配</strong>：70%预算给高价值+潜力用户，确保ROI健康</li>
                <li><strong>LTV思维</strong>：关注用户全生命周期价值，而非单次GMV，长期价值>短期增长</li>
                <li><strong>补贴成本控制</strong>：精准补贴>普惠补贴，设定ROI阈值（1:3），渐进式补贴策略，避免无底洞烧钱</li>
                <li><strong>补贴案例启示</strong>：拼多多（LTV/CAC=3.5成功）vs 淘特（获客成本>LTV失败），数据是补贴的方向盘</li>
                <li><strong>良性竞争路径</strong>：从价格战到价值战，差异化竞争、用户体验、会员体系、精准运营</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Tab5: 支付生态讨论要点
        st.markdown("### 💳 支付生态布局讨论要点")
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 18px; border-radius: 8px; margin-bottom: 20px;">
            <h4 style="color: #1976d2; margin: 0 0 12px 0;">核心观点</h4>
            <ul style="color: #424242; line-height: 1.8;">
                <li><strong>战略意义</strong>：支付不只是交易工具，更是数据资产和生态闭环的关键环节</li>
                <li><strong>市场机会</strong>：抖音月活10.2亿+，若支付渗透率达50%，可贡献2.1万亿+支付规模</li>
                <li><strong>三重价值</strong>：
                    <ul>
                        <li><strong>经济价值</strong>：手续费收入（年GMV 4.2万亿×50%×0.1%≈21亿）+ 资金沉淀收益</li>
                        <li><strong>数据价值</strong>：完整交易链路数据，增强用户画像和风控能力</li>
                        <li><strong>生态价值</strong>：降低对第三方依赖，提升用户粘性，拓展场景</li>
                    </ul>
                </li>
                <li><strong>双11推广策略</strong>：首次绑卡奖励、支付立减、抽奖、时段加码等激励措施</li>
                <li><strong>监测指标</strong>：渗透率（目标35%）、活跃度（人均2.5笔）、留存（65%）、交易规模（GMV占比25%）</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Tab6: 产品体验观察讨论要点
        st.markdown("### 🤔 产品体验观察讨论要点")
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 18px; border-radius: 8px; margin-bottom: 20px;">
            <h4 style="color: #1976d2; margin: 0 0 12px 0;">核心观点</h4>
            <ul style="color: #424242; line-height: 1.8;">
                <li><strong>APP性能问题</strong>：卡顿影响转化率（页面加载时间每增加1秒，转化率可能下降7%），需建立性能监控看板</li>
                <li><strong>超级APP思考</strong>：
                    <ul>
                        <li><strong>优势</strong>：数据闭环、用户画像增强、交叉销售、LTV提升</li>
                        <li><strong>挑战</strong>：性能问题、用户认知混乱、核心业务稀释、运营复杂度</li>
                        <li><strong>建议</strong>：场景协同而非简单堆砌，用数据验证场景间协同效应（如直播→电商转化率>30%才有价值）</li>
                    </ul>
                </li>
                <li><strong>用户反馈机制</strong>：长按反馈功能体验不佳，需要优化</li>
                <li><strong>批判性思维</strong>：不盲目追随行业趋势，基于数据评估是否适合自身</li>
                <li><strong>数据产品思维</strong>：从用户体验问题出发，用数据量化、分析、验证、优化</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 候选人优势总结
        st.markdown("---")
        st.markdown("""
        <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; border-left: 5px solid #ff9800; margin-top: 25px;">
            <h4 style="color: #e65100; margin: 0 0 15px 0;">👤 候选人能力展示维度</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div>
                    <p style="color: #424242; margin: 5px 0;"><strong>📊 数据分析能力</strong></p>
                    <ul style="font-size: 14px; color: #616161; margin: 5px 0;">
                        <li>市场数据收集与分析</li>
                        <li>用户行为数据洞察</li>
                        <li>AB测试设计与解读</li>
                    </ul>
                </div>
                <div>
                    <p style="color: #424242; margin: 5px 0;"><strong>🎯 产品思维</strong></p>
                    <ul style="font-size: 14px; color: #616161; margin: 5px 0;">
                        <li>实际用户体验观察</li>
                        <li>产品功能理解与分析</li>
                        <li>用户需求挖掘</li>
                    </ul>
                </div>
                <div>
                    <p style="color: #424242; margin: 5px 0;"><strong>🔬 实验设计能力</strong></p>
                    <ul style="font-size: 14px; color: #616161; margin: 5px 0;">
                        <li>AB测试方案设计</li>
                        <li>指标体系构建</li>
                        <li>因果推断理解</li>
                    </ul>
                </div>
                <div>
                    <p style="color: #424242; margin: 5px 0;"><strong>💼 商业洞察</strong></p>
                    <ul style="font-size: 14px; color: #616161; margin: 5px 0;">
                        <li>市场竞争格局分析</li>
                        <li>商业模式理解</li>
                        <li>战略思考能力</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- Page 3: 对比与发展 ----------------
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

# ---------------- Page 7: MTA归因模型项目 ---------------- 
elif page == "MTA归因模型AB测试":
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
        Demo by 侯良语 | 2025-10-09
    </div>
    """, 
    unsafe_allow_html=True
)