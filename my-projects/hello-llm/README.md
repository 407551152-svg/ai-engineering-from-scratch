# Hello LLM

这是我的第一个大模型调用小项目。

## 目标

- 学会读取环境变量
- 学会创建 OpenAI 客户端
- 学会发送 messages
- 学会打印模型回复

## 运行方式

```powershell
$env:OPENAI_API_KEY="你的APIKey"
$env:OPENAI_MODEL="gpt-4o-mini"
python my-projects/hello-llm/main.py