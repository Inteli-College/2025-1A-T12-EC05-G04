// src/components/Layout.jsx
import SideBar from './Sidebar';

export default function Layout({ children }) {
  return (
    <div className="layout-container">
      <SideBar />
      <main className="main-content">
        {children}
      </main>
    </div>
  );
}