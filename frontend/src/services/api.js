import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getThreads = async () => {
  const response = await API.get("/threads");
  return response.data;
};

export const getAgentReply = async (threadId) => {
  const response = await API.get(
    `/agent-reply/${threadId}`
  );

  return response.data;
};

export const getThreadMessages = async (threadId) => {
  const response = await API.get(
    `/threads/${threadId}`
  );

  return response.data;
};

export const getAgentAnalysis = async (threadId) => {
  const response = await API.get(
    `/agent-reply/${threadId}`
  );

  return response.data;
};