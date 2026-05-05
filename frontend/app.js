let editor;

require.config({ paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs' }});

require(['vs/editor/editor.main'], function () {
  editor = monaco.editor.create(document.getElementById('editor'), {
    value: "# Write code here...",
    language: "python",
    theme: "vs-dark"
  });
});

// FILE UPLOAD + LANGUAGE DETECT
document.getElementById("fileInput").addEventListener("change", async (e) => {
  const file = e.target.files[0];
  const text = await file.text();

  editor.setValue(text);

  const ext = file.name.split('.').pop();

  let lang = "python";
  if (ext === "js") lang = "javascript";
  if (ext === "cpp") lang = "cpp";
  if (ext === "java") lang = "java";

  monaco.editor.setModelLanguage(editor.getModel(), lang);
});

// ANALYZE
async function analyze() {
  document.getElementById("loader").classList.remove("hidden");

  const code = editor.getValue();

  const res = await fetch("https://ai-code-analyzer.onrender.com/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ code, language: "python" })
  });

  const data = await res.json();

  // SCORE BAR
  document.getElementById("scoreFill").style.width = `${data.score * 10}%`;

  let output = `⭐ Score: ${data.score}/10\n\n`;

  output += "⚠️ Issues:\n";
  data.issues.forEach(i => {
    output += `Line ${i.line}: ${i.message}\n`;
  });

  output += "\n🤖 AI Suggestions:\n" + data.ai;

  document.getElementById("output").textContent = output;

  document.getElementById("loader").classList.add("hidden");
}

// COPY
function copyOutput() {
  const text = document.getElementById("output").textContent;
  navigator.clipboard.writeText(text);
}

// THEME TOGGLE
function toggleTheme() {
  document.body.classList.toggle("light");

  if (document.body.classList.contains("light")) {
    localStorage.setItem("theme", "light");
  } else {
    localStorage.setItem("theme", "dark");
  }
}

// LOAD THEME
window.onload = () => {
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme === "light") {
    document.body.classList.add("light");
  }
};