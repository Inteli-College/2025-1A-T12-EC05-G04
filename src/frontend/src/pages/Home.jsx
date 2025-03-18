import React from 'react';
import SideBar from "./components/Sidebar";

export default function Home() {
  return (
    <div className="screen">
      <SideBar />
      <div className="home"></div>
    </div>
  );
}