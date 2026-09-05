"""Main React Component - المكون الرئيسي للـ React"""

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Globe } from './components/Globe';
import { EntityTracker } from './components/EntityTracker';
import { AlertPanel } from './components/AlertPanel';
import { IntelligenceDashboard } from './components/IntelligenceDashboard';
import './App.css';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [selectedEntity, setSelectedEntity] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [entities, setEntities] = useState([]);
  const [viewMode, setViewMode] = useState('3d'); // 3d, 2d, satellite

  useEffect(() => {
    // Fetch initial data
    fetchEntities();
    fetchAlerts();

    // Set up WebSocket for live updates
    const ws = new WebSocket(`${API_BASE_URL.replace('http', 'ws')}/api/v1/intelligence/ws/live-alerts`);
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'alert_update') {
        setAlerts(data.alerts);
      }
    };

    return () => ws.close();
  }, []);

  const fetchEntities = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/v1/intelligence/entities`);
      setEntities(response.data.entities);
    } catch (error) {
      console.error('Error fetching entities:', error);
    }
  };

  const fetchAlerts = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/v1/intelligence/alerts`);
      setAlerts(response.data.alerts);
    } catch (error) {
      console.error('Error fetching alerts:', error);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🛰️ God's Eye View - Satellite Intelligence Platform</h1>
        <div className="view-controls">
          <button onClick={() => setViewMode('3d')} className={viewMode === '3d' ? 'active' : ''}>3D Globe</button>
          <button onClick={() => setViewMode('2d')} className={viewMode === '2d' ? 'active' : ''}>2D Map</button>
          <button onClick={() => setViewMode('satellite')} className={viewMode === 'satellite' ? 'active' : ''}>Satellite</button>
        </div>
      </header>

      <div className="main-content">
        <div className="map-container">
          {viewMode === '3d' ? (
            <Globe entities={entities} selectedEntity={selectedEntity} />
          ) : (
            <div className="placeholder-map">2D Map View - Coming Soon</div>
          )}
        </div>

        <aside className="sidebar">
          <IntelligenceDashboard entities={entities} alerts={alerts} />
          <EntityTracker entities={entities} onSelectEntity={setSelectedEntity} />
          <AlertPanel alerts={alerts} />
        </aside>
      </div>
    </div>
  );
}

export default App;
