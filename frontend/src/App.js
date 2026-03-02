import { useState } from "react";
import "./index.css";

const API_BASE = "http://127.0.0.1:5000";

function App() {
  const [roleName, setRoleName] = useState("");
  const [permissionName, setPermissionName] = useState("");
  const [assignRole, setAssignRole] = useState("");
  const [assignPermission, setAssignPermission] = useState("");

  const [username, setUsername] = useState("");
  const [userRole, setUserRole] = useState("");

  const [deleteUser, setDeleteUser] = useState("");
  const [message, setMessage] = useState("");

  const createPermission = async () => {
    const res = await fetch(`${API_BASE}/permission`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: permissionName }),
    });
    const data = await res.json();
    setMessage(data.message || data.error);
  };

  const createRole = async () => {
    const res = await fetch(`${API_BASE}/role`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: roleName }),
    });
    const data = await res.json();
    setMessage(data.message || data.error);
  };

  const assignPermissionToRole = async () => {
  const res = await fetch(`${API_BASE}/assign-permission`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      role_name: assignRole,
      permission_name: assignPermission,
    }),
  });

  const data = await res.json();

  if (!res.ok) {
    setMessage("❌ " + (data.error || "Something went wrong"));
  } else {
    setMessage("✅ " + data.message);
  }
};

  const createUser = async () => {
    const res = await fetch(`${API_BASE}/user`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: username,
        role_name: userRole,
      }),
    });
    const data = await res.json();
    setMessage(data.message || data.error);
  };

  const deleteUserAction = async () => {
    const res = await fetch(`${API_BASE}/delete-user`, {
      method: "POST",
      headers: {
        "X-Username": deleteUser,
      },
    });
    const data = await res.json();
    setMessage(data.message || data.error);
  };

  return (
    <div className="container">
      <div className="card">
        <h1>RBAC Management Dashboard</h1>
        <p className="subtitle">Role-Based Access Control System</p>

        <div className="section">
          <h3>Create Permission</h3>
          <input
            placeholder="Permission name"
            value={permissionName}
            onChange={(e) => setPermissionName(e.target.value)}
          />
          <button onClick={createPermission}>Create Permission</button>
        </div>

        <div className="section">
          <h3>Create Role</h3>
          <input
            placeholder="Role name"
            value={roleName}
            onChange={(e) => setRoleName(e.target.value)}
          />
          <button onClick={createRole}>Create Role</button>
        </div>

        <div className="section">
          <h3>Assign Permission to Role</h3>
          <input
            placeholder="Role name"
            value={assignRole}
            onChange={(e) => setAssignRole(e.target.value)}
          />
          <input
            placeholder="Permission name"
            value={assignPermission}
            onChange={(e) => setAssignPermission(e.target.value)}
          />
          <button onClick={assignPermissionToRole}>
            Assign Permission
          </button>
        </div>

        <div className="section">
          <h3>Create User</h3>
          <input
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            placeholder="Role name"
            value={userRole}
            onChange={(e) => setUserRole(e.target.value)}
          />
          <button onClick={createUser}>Create User</button>
        </div>

        <div className="section">
          <h3>Test Delete Permission</h3>
          <input
            placeholder="Username"
            value={deleteUser}
            onChange={(e) => setDeleteUser(e.target.value)}
          />
          <button className="danger" onClick={deleteUserAction}>
            Delete User
          </button>
        </div>

        {message && (
          <div style={{ marginTop: "20px", fontWeight: "bold" }}>
            {message}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;