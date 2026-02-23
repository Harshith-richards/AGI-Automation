import { Link, Route, Routes } from 'react-router-dom';

const Dashboard = () => <div>Dashboard: live tasks and metrics.</div>;
const Tasks = () => <div>Task interface with DAG execution stream.</div>;
const Agents = () => <div>Agent monitor.</div>;
const Memory = () => <div>Memory explorer and graph.</div>;
const Tools = () => <div>Tool registry.</div>;
const Settings = () => <div>Settings.</div>;

export function App() {
  return (
    <div style={{ padding: 16, fontFamily: 'sans-serif' }}>
      <h1>NEXUS-AGI</h1>
      <nav style={{ display: 'flex', gap: 8 }}>
        <Link to='/'>Dashboard</Link><Link to='/tasks'>Tasks</Link><Link to='/agents'>Agents</Link><Link to='/memory'>Memory</Link><Link to='/tools'>Tools</Link><Link to='/settings'>Settings</Link>
      </nav>
      <Routes>
        <Route path='/' element={<Dashboard />} />
        <Route path='/tasks' element={<Tasks />} />
        <Route path='/agents' element={<Agents />} />
        <Route path='/memory' element={<Memory />} />
        <Route path='/tools' element={<Tools />} />
        <Route path='/settings' element={<Settings />} />
      </Routes>
    </div>
  );
}
