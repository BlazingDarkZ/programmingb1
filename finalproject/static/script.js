const API = "http://127.0.0.1:8000";

async function loadTasks() {
    const res = await fetch(`${API}/tasks`);
    const tasks = await res.json();
    renderTasks(tasks);
    loadStats();
}

async function filterTasks(status) {
    const res = await fetch(`${API}/tasks?completed=${status}`);
    const tasks = await res.json();
    renderTasks(tasks);
}

function renderTasks(tasks) {
    const table = document.getElementById("taskTable");
    table.innerHTML = "";

    tasks.forEach(task => {
        table.innerHTML += `
            <tr>
                <td>${task.title}</td>
                <td>${task.description || ""}</td>
                <td>${task.completed ? "✅ Completed" : "⏳ Pending"}</td>
                <td>
                    <button onclick="toggleTask(${task.id}, ${task.completed})">Toggle</button>
                    <button onclick="deleteTask(${task.id})">Delete</button>
                </td>
            </tr>
        `;
    });
}

async function createTask() {
    const title = document.getElementById("titleInput").value;
    const description = document.getElementById("descInput").value;

    await fetch(`${API}/tasks`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description })
    });

    closeModal();
    loadTasks();
}

async function toggleTask(id, completed) {
    const res = await fetch(`${API}/tasks/${id}`);
    const task = await res.json();

    task.completed = !completed;

    await fetch(`${API}/tasks/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task)
    });

    loadTasks();
}

async function deleteTask(id) {
    await fetch(`${API}/tasks/${id}`, { method: "DELETE" });
    loadTasks();
}

async function loadStats() {
    const res = await fetch(`${API}/tasks/stats`);
    const stats = await res.json();

    document.getElementById("totalCount").innerText = stats.total_tasks;
    document.getElementById("completedCount").innerText = stats.completed_tasks;
    document.getElementById("pendingCount").innerText = stats.pending_tasks;
}

function showCreateForm() {
    document.getElementById("taskModal").classList.remove("hidden");
}

function closeModal() {
    document.getElementById("taskModal").classList.add("hidden");
}

loadTasks();

async function showStats() {
    try {
        const res = await fetch("/tasks/stats");

        if (!res.ok) {
            alert("Stats endpoint error");
            return;
        }

        const stats = await res.json();

        // Debug check (optional)
        console.log(stats);

        document.getElementById("statTotal").innerText = stats.total_tasks ?? 0;
        document.getElementById("statCompleted").innerText = stats.completed_tasks ?? 0;
        document.getElementById("statPending").innerText = stats.pending_tasks ?? 0;

        const percent = stats.completion_percentage ?? 0;
        document.getElementById("statPercent").innerText = percent.toFixed(1) + "%";

        // Animate ring safely
        const circle = document.getElementById("progressCircle");
        const radius = 50;
        const circumference = 2 * Math.PI * radius;

        circle.style.strokeDasharray = circumference;

        const offset = circumference - (percent / 100) * circumference;
        circle.style.strokeDashoffset = offset;

        document.getElementById("statsModal").classList.remove("hidden");

    } catch (error) {
        console.error("Stats error:", error);
        alert("Something went wrong loading stats.");
    }
}

let allTasks = [];

async function loadTasks() {
    const res = await fetch(`${API}/tasks`);
    const tasks = await res.json();
    allTasks = tasks;
    renderTasks(tasks);
    loadStats();
}

function searchTasks() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = allTasks.filter(task =>
        task.title.toLowerCase().includes(query) ||
        (task.description && task.description.toLowerCase().includes(query))
    );
    renderTasks(filtered);
}

function closeStats() {
    document.getElementById("statsModal").classList.add("hidden");
}