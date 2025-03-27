// __tests__/HomePage.test.jsx
import React from 'react';
import { render, screen, act } from '@testing-library/react';
import HomePage from '../pages/HomePage';
import { io } from 'socket.io-client';

// Mock do socket.io
jest.mock('socket.io-client');

describe('HomePage WebSocket integration', () => {
  let mockSocket;

  beforeEach(() => {
    mockSocket = {
      on: jest.fn(),
      emit: jest.fn(),
      disconnect: jest.fn()
    };

    io.mockReturnValue(mockSocket);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('deve renderizar log recebido do WebSocket', async () => {
    const logHandler = {};

    // Simula registros do método .on()
    mockSocket.on.mockImplementation((event, cb) => {
      logHandler[event] = cb;
    });

    render(<HomePage />);

    const fakeLog = {
      medicineName: 'Dipirona',
      progress: 60,
      message: 'Medicamento processado'
    };

    // Dispara evento 'log'
    await act(() => {
      logHandler['log'](fakeLog);
      return Promise.resolve();
    });

    // Verifica se o conteúdo foi exibido corretamente
    expect(screen.getByText(/Dipirona/)).toBeInTheDocument();
    expect(screen.getByText(/60%/)).toBeInTheDocument();
    expect(screen.getByText(/Medicamento processado/)).toBeInTheDocument();
  });
});
