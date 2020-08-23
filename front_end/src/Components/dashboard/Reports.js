import React, { PureComponent, useState} from 'react';
import {
  BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';
import Paper from "@material-ui/core/Paper";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/BUtton";


export default function Charts(props){
    const mapData = (data) => {
        let map = {}
        for (let v of data){
            if (map[v["ourCategory"]] === undefined)
                map[v["ourCategory"]] = 0;
            else 
                map[v["ourCategory"]] += v["amount"];
        }
        
        return Object.keys(map).map((k, i) => (
            {
                name: k,
                amount : map[k]
            }
        ));
    }; 

    const [data, setData] = useState(mapData(props.transactions));
    console.log(data);
    return (
      <BarChart
        width={500}
        height={300}
        data={data}
        margin={{
          top: 5, right: 30, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="amount" fill="#82ca9d" />
      </BarChart>
    );
}