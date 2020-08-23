import React, { useState } from 'react';
import Paper from '@material-ui/core/Paper';
import {
  Grid,
  Table,
  TableHeaderRow,
} from '@devexpress/dx-react-grid-material-ui';


export default (props) => {
  const mapData = (data) => (
    data.map((v, i) => ({ 
      id: i,
      description: v["name"],
      amount: v["amount"],
      date: v["date"],
      category : v["category"].join(" / "),
  }))
  );
  const [columns] = useState([
      {name : "description", title : "Description"},
      {name : "amount", title : "Amount"},
      {name : "date", title : "Date"},
      {name : "category", title : "Category"}
  ]);
  const [rows] = useState(mapData(props.data));

  console.log(rows);
  return (
    <Paper>
      <Grid
        rows={rows}
        columns={columns}
      >
        <Table />
        <TableHeaderRow />
      </Grid>
    </Paper>
  );
};