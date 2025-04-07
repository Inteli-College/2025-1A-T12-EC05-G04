import {
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    PieChart,
    Pie,
    Cell,
    Legend
  } from "recharts";
  import styles from "../../styles/Graficos.module.css";
  
  export default function Graficos() {
    const areaData = [
      { tempo: "Jan", fita1: 10, fita2: 5, fita3: 3 },
      { tempo: "Fev", fita1: 20, fita2: 8, fita3: 6 },
      { tempo: "Mar", fita1: 30, fita2: 12, fita3: 9 },
      { tempo: "Abr", fita1: 50, fita2: 20, fita3: 15 },
      { tempo: "Mai", fita1: 70, fita2: 30, fita3: 22 },
    ];
  
    const pieData = [
      { name: "Pediatria", value: 400 },
      { name: "UTI", value: 300 },
      { name: "Cardiologia", value: 200 },
      { name: "Neurologia", value: 150 },
      { name: "Ortopedia", value: 100 },
    ];
  
    const COLORS = ["#d1d5db", "#a1a1aa", "#6b7280", "#4b5563", "#374151"];
  
    return (
      <div className='graficos-container'>
        <div className="grafico-item">
          <h3>Fitas montadas x tempo</h3>
          <AreaChart
            width={400}
            height={250}
            data={areaData}
            margin={{ top: 10, right: 0, left: 0, bottom: 0 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="tempo" />
            <YAxis />
            <Tooltip />
            <Area type="monotone" dataKey="fita1" stackId="1" stroke="#6b7280" fill="#9ca3af" />
            <Area type="monotone" dataKey="fita2" stackId="1" stroke="#4b5563" fill="#6b7280" />
            <Area type="monotone" dataKey="fita3" stackId="1" stroke="#374151" fill="#4b5563" />
          </AreaChart>
        </div>
  
        <div className="grafico-item">
          <h3>Alas com mais fitas médicas</h3>
          <PieChart width={400} height={250}>
            <Pie
              data={pieData}
              cx="50%"
              cy="50%"
              labelLine={false}
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
            >
              {pieData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Legend layout="vertical" align="right" verticalAlign="middle" />
            <Tooltip />
          </PieChart>
        </div>
      </div>
    );
  }
  