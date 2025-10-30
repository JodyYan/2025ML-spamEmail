# OpenSpec 代理商工作流 (OpenSpec Agent Workflow)

本專案使用 OpenSpec 進行開發。代理商（AI 助手）應遵循以下循環：

1.  **閱讀 `project.md`:** 了解專案的整體背景、技術棧和目標。
2.  **接收提案 (Proposal):** 接收並確認用戶發起的新功能或變更提案。
3.  **生成規範 (`proposal.md`, `tasks.md`):** 將用戶的自然語言需求轉換為詳細的、可執行的技術任務清單。
4.  **執行任務 (Apply):** 根據 `tasks.md` 中的步驟，逐一實施程式碼更改。
5.  **歸檔 (Archive):** 變更完成後，將所有相關文件移至 `ARCHIVE/` 資料夾，並更新 `project.md`（如果需要）。
6.  **版本控制 (Git):** 每次歸檔後，將更改提交至 Git 儲存庫。