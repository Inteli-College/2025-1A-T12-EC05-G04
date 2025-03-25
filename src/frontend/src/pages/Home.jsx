import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import SideBar from './components/Sidebar'; // Assumindo que você tem um componente SideBar

const SystemStatusBar = ({ robotStatus, assemblyStatus }) => {
  const getStatusClass = (status) => 
    status ? 'bg-green-500 text-white' : 'bg-red-500 text-white';

  return (
    <div className="flex justify-between items-center p-4 bg-gray-100 rounded-t-lg">
      <div className="flex items-center space-x-4">
        <div className={`px-3 py-1 rounded ${getStatusClass(robotStatus)}`}>
          Robô: {robotStatus ? 'Ativo' : 'Inativo'}
        </div>
        <div className={`px-3 py-1 rounded ${getStatusClass(assemblyStatus)}`}>
          Montagem: {assemblyStatus ? 'Ativa' : 'Inativa'}
        </div>
      </div>
    </div>
  );
};

export default function HomePage() {
  const [systemStatus, setSystemStatus] = useState({
    robotStatus: false,
    assemblyStatus: false,
    pendingListApproved: false
  });

  const toggleRobotStatus = () => {
    setSystemStatus(prev => ({
      robotStatus: !prev.robotStatus,
      assemblyStatus: false,
      pendingListApproved: false
    }));
  };

  const toggleAssemblyStatus = () => {
    if (systemStatus.robotStatus) {
      setSystemStatus(prev => ({
        ...prev,
        assemblyStatus: false,
        pendingListApproved: false
      }));
    }
  };

  const approvePendingList = () => {
    setSystemStatus(prev => ({
      ...prev,
      pendingListApproved: true,
      assemblyStatus: true
    }));
  };

  const ButtonBar = () => {
    const { robotStatus, assemblyStatus } = systemStatus;

    // Lógica para renderizar botões baseado no estado atual
    if (!robotStatus && !assemblyStatus) {
      return (
        <div className="w-full bg-gray-200 p-4 flex justify-center items-center">
          <h2>Status: </h2>
          <button 
            onClick={toggleRobotStatus}
            className="bg-green-500 text-white px-6 py-3 rounded-lg hover:bg-green-600 transition-colors"
          >
            Off
          </button>
        </div>
      );
    }

    if (robotStatus && !assemblyStatus) {
      return (
        <div className="w-full bg-gray-200 p-4 flex justify-center items-center space-x-4">
          <h2>Status</h2>
          <button 
            onClick={toggleRobotStatus}
            className="bg-red-500 text-white px-6 py-3 rounded-lg hover:bg-red-600 transition-colors"
          >
            On
          </button>
          <button 
            onClick={approvePendingList}
            className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition-colors"
          >
            Off
          </button>
        </div>
      );
    }

    if (robotStatus && assemblyStatus) {
      return (
        <div className="w-full bg-gray-200 p-4 grid grid-cols-2 gap-4">
          <h2>Status:</h2>
          <button 
            onClick={toggleRobotStatus}
            className="bg-red-500 text-white px-6 py-3 rounded-lg hover:bg-red-600 transition-colors"
          >
            On
          </button>
          <button 
            onClick={toggleAssemblyStatus}
            className="bg-red-500 text-white px-6 py-3 rounded-lg hover:bg-red-600 transition-colors"
          >
            On
          </button>
        </div>
      );
    }

    return null;
  };

  const MainContent = () => {
    const { robotStatus, assemblyStatus } = systemStatus;

    // Variante 1: Off/Off
    if (!robotStatus && !assemblyStatus) {
      return (
        <div className="flex flex-col items-center justify-center min-h-[calc(100vh-200px)] text-center p-4">
          <h2 className="text-2xl font-bold mb-4">Sistema Inativo</h2>
          <p className="mb-6 text-gray-600">Para iniciar, ligue o robô</p>
        </div>
      );
    }

    // Variante 2: On/Off
    if (robotStatus && !assemblyStatus) {
      return (
        <div className="flex flex-col items-center justify-center min-h-[calc(100vh-200px)] text-center p-4">
          <h2 className="text-2xl font-bold mb-4">Robô Ativo</h2>
          <p className="mb-6 text-gray-600">
            Para iniciar a montagem de uma fita, aprove as listas pendentes
          </p>
        </div>
      );
    }

    // Variante 3: On/On
    if (robotStatus && assemblyStatus) {
      return (
        <div className="min-h-[calc(100vh-200px)] p-4">
          <h2 className="text-2xl font-bold mb-4">Sistema Totalmente Operacional</h2>
          <div className="bg-gray-100 p-4 rounded-lg">
            <p>Conteúdo da terceira variante será adicionado aqui</p>
          </div>
        </div>
      );
    }

    return null;
  };

  return (
    <div className="screen">
      <SideBar />
      <div className='content flex flex-col'>
        <SystemStatusBar 
          robotStatus={systemStatus.robotStatus}
          assemblyStatus={systemStatus.assemblyStatus}
        />
        <ButtonBar />
        <MainContent />
      </div>
    </div>
  );
}