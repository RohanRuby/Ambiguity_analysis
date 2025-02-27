import google.generativeai as genai


# 配置 Gemini API Key
GEMINI_API_KEY = "AIzaSyB_9bXwyTF4vGNEoFC9UnjN8vKGOrb2E4U"
genai.configure(api_key=GEMINI_API_KEY)



def check_ambiguity(sentence):
    """调用 Gemini API 进行歧义分析"""
    prompt = f"请分析以下汉语句子的歧义，并给出可能的不同理解：\n\n句子：{sentence}\n\n分析："
    
    # 使用可用模型之一（推荐用最新的）
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  
    response = model.generate_content(prompt)

    return response.text if response else "无法解析该句子"

def process_file(input_file, output_file):
    """读取输入文件，调用 API 处理文本，并保存结果"""
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            sentence = line.strip()
            if sentence:  # 跳过空行
                print(f"处理句子: {sentence}")
                result = check_ambiguity(sentence)
                outfile.write(f"输入: {sentence}\n分析: {result}\n\n")

# 批量处理文本文件
input_file = "input.txt"   # 输入文件（每行一个句子）
output_file = "output.txt" # 结果保存文件
process_file(input_file, output_file)

print("处理完成，结果已保存到 output.txt")
