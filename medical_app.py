import streamlit as st
import pandas as pd
import time
from PIL import Image

# ==========================================
# 0. 全局页面配置 (必须放在最开头)
# ==========================================
st.set_page_config(
    page_title="智能医学系统概览", 
    page_icon="🏥", 
    layout="wide"
)

# ==========================================
# 1. 侧边栏导航设计 (Sidebar)
# ==========================================
st.sidebar.title("🏥 智能医学辅助系统")
st.sidebar.markdown("---")
# 定义三个模块
menu = ["🏠 课程与技术简介", "📊 电子病历数据分析", "🔬 影像智能诊断体验"]
choice = st.sidebar.radio("请选择系统功能模块", menu)

st.sidebar.markdown("---")
st.sidebar.info("欢迎来到《智能医学诊断技术》第一课！")

# ==========================================
# 2. 模块一：首页（排版、文本、图片布局）
# ==========================================
if choice == "🏠 课程与技术简介":
    st.title("欢迎探索《智能医学诊断技术》 🧬")
    st.markdown("### AI 赋能现代医疗的奇妙旅程")
    
    # 使用 columns 将页面分为左右两列
    col1, col2 = st.columns([6, 4]) # 6:4的宽度比例
    
    with col1:
        st.write("#### 💡 什么是智能医学？")
        st.write("""
        智能医学是计算机科学与临床医学的深度交叉。通过引入**人工智能、大数据分析、计算机视觉**等前沿技术，
        我们能够让计算机“看懂”医学影像、“读懂”病历文书，从而辅助医生做出更精准、更高效的诊断。
        """)
        st.success("本课程目标：让医学生懂AI，让工科生懂医学，成为复合型人才！")
        
        st.write("#### 🎯 主要应用场景：")
        st.write("- 🩻 **计算机视觉**：X光、CT、病理切片的病灶检测与分割。")
        st.write("- 📝 **自然语言处理(NLP)**：结构化电子病历，智能分诊。")
        st.write("- 🧬 **预测模型**：疾病风险预警与患者生存期预测。")

    with col2:
        # 使用网络图片展示科技感（学生也可以下载本地图片使用相对路径）
        img_url = "https://images.unsplash.com/photo-1576091160550-2173ff9e5ee5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        st.image(img_url, caption="AI 医疗未来", use_container_width=True)

# ==========================================
# 3. 模块二：数据展示（Pandas与图表）
# ==========================================
elif choice == "📊 电子病历数据分析":
    st.title("📊 模拟临床病历数据(EMR)分析")
    st.write("深度学习离不开数据。这里展示如何使用 Streamlit 快速查看和分析患者队列。")
    
    # 构造一个模拟的患者字典数据
    patient_data = {
        "患者ID":["P001", "P002", "P003", "P004", "P005", "P006"],
        "年龄":[45, 62, 34, 78, 29, 55],
        "性别":["男", "女", "男", "女", "女", "男"],
        "收缩压(mmHg)":[120, 145, 110, 160, 115, 135],
        "AI评估风险": ["低", "高", "低", "极高", "低", "中"]
    }
    # 转化为 DataFrame
    df = pd.DataFrame(patient_data)
    
    # 展示数据表格 (交互式表格)
    st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📈 数据可视化：患者年龄与血压关系")
    
    # 绘制折线图，展示年龄和血压的趋势
    chart_data = df[["年龄", "收缩压(mmHg)"]].set_index("年龄")
    st.line_chart(chart_data)

# ==========================================
# 4. 模块三：核心体验（文件上传与交互模拟）
# ==========================================
elif choice == "🔬 影像智能诊断体验":
    st.title("🔬 肺部影像智能辅助诊断系统 (Demo)")
    st.info("请尝试上传一张包含肺部的 X光片或 CT 图像（您可以从网上随意下载一张作为测试）。")
    
    # 1. 文件上传组件
    uploaded_file = st.file_uploader("📂 选择医学影像图片进行上传", type=["jpg", "png", "jpeg"])
    
    # 当用户上传了文件后
    if uploaded_file is not None:
        # 使用 PIL 读取图像
        image = Image.open(uploaded_file)
        
        # 再次分左右列，左边看原图，右边出结果
        col_img, col_res = st.columns(2)
        
        with col_img:
            st.subheader("原始输入影像")
            st.image(image, caption="待诊断影像", use_container_width=True)
            
        with col_res:
            st.subheader("AI 诊断面板")
            # 2. 交互按钮
            if st.button("🚀 启动深度学习模型分析"):
                
                # 3. 模拟 AI 运算过程 (使用进度条)
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # 模拟特征提取的循环耗时
                for percent_complete in range(100):
                    time.sleep(0.03) # 模拟模型推理耗时
                    progress_bar.progress(percent_complete + 1)
                    if percent_complete < 30:
                        status_text.text("🔄 正在加载 ResNet 模型权重...")
                    elif percent_complete < 70:
                        status_text.text("🔍 正在提取肺部纹理特征...")
                    else:
                        status_text.text("⚙️ 正在生成分类热力图与诊断报告...")
                
                # 运算结束，清空进度条提示
                status_text.empty()
                
                # 4. 输出模拟的诊断结果
                st.success("✅ AI 分析已完成！")
                st.markdown("""
                ### 📄 自动生成的辅助诊断报告
                * **模型置信度**：`98.7%`
                * **病灶定位**：未见明显磨玻璃结节或大面积实变。
                * **AI 建议**：双肺野清晰，心影大小形态正常。当前影像**无明显异常**，建议结合临床症状综合判断。
                
                > ⚠️ **声明**：本结果由《智能医学诊断技术》第一课模拟生成，不具备真实临床法律效力。
                """)