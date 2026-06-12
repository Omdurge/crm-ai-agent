function ThreadDetails({
  messages,
  analysis,
}) {
  if (!messages.length) {
    return (
      <div>
        Select a thread
      </div>
    );
  }

  return (
    <div>
      <h2>Conversation</h2>

      {messages.map((msg) => (
        <div
          key={msg.message_id}
          style={{
            border: "1px solid #444",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          <b>{msg.sender}</b>

          <p>{msg.subject}</p>

          <p>{msg.body}</p>
        </div>
      ))}

      {analysis && (
        <>
          <h2>Classification</h2>

          <pre>
            {JSON.stringify(
              analysis.classification,
              null,
              2
            )}
          </pre>

          <h2>Decision</h2>

          <pre>
            {JSON.stringify(
              analysis.decision,
              null,
              2
            )}
          </pre>
        </>
      )}
    </div>
  );
}

export default ThreadDetails;