import { useEffect, useState } from "react";

import {
  getThreads,
  getThreadMessages,
  getAgentAnalysis,
} from "../services/api";

import ThreadDetails from "../components/ThreadDetails";

function ThreadsPage() {
  const [threads, setThreads] = useState([]);

  const [selectedThread, setSelectedThread] =
    useState(null);

  const [messages, setMessages] = useState([]);

  const [analysis, setAnalysis] =
    useState(null);

  const [loading, setLoading] =
    useState(false);

  useEffect(() => {
    loadThreads();
  }, []);

  async function loadThreads() {
    try {
      const data = await getThreads();
      setThreads(data);
    } catch (error) {
      console.error(error);
    }
  }

  async function selectThread(threadId) {
    setSelectedThread(threadId);

    setLoading(true);

    setMessages([]);
    setAnalysis(null);

    try {
      const [threadMessages, agentData] =
        await Promise.all([
          getThreadMessages(threadId),
          getAgentAnalysis(threadId),
        ]);

      setMessages(threadMessages);

      setAnalysis(agentData);

    } catch (error) {
      console.error(
        "Failed to load thread:",
        error
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        backgroundColor: "#0f172a",
        color: "white",
      }}
    >
      {/* LEFT PANEL */}

      <div
        style={{
          width: "35%",
          overflowY: "auto",
          borderRight: "1px solid #333",
          padding: "20px",
        }}
      >
        <h1>CRM AI Agent</h1>

        {threads.map((thread) => (
          <div
            key={thread.thread_id}
            onClick={() =>
              selectThread(thread.thread_id)
            }
            style={{
              border: "1px solid #444",
              padding: "12px",
              marginBottom: "10px",
              borderRadius: "8px",
              cursor: "pointer",
              background:
                selectedThread ===
                thread.thread_id
                  ? "#1e293b"
                  : "transparent",
            }}
          >
            <h3>{thread.subject}</h3>

            <p>{thread.sender}</p>

            <small>{thread.thread_id}</small>
          </div>
        ))}
      </div>

      {/* RIGHT PANEL */}

      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: "20px",
        }}
      >
        {loading ? (
          <h2>Loading...</h2>
        ) : (
          <ThreadDetails
            messages={messages}
            analysis={analysis}
          />
        )}
      </div>
    </div>
  );
}

export default ThreadsPage;