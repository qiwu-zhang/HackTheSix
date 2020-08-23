import React from "react"; 
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import { Grid } from "@material-ui/core";
import Paper from '@material-ui/core/Paper';
import CssBaseline from '@material-ui/core/CssBaseline';
import Chart from './Chart';
import Deposits from './Deposits';
import Orders from './Orders';
import ButtonGroup from "@material-ui/core/ButtonGroup"
import Box from '@material-ui/core/Box';

const useStyles = makeStyles((theme) => ({
    paper : {
        padding: theme.spacing(2),
        display: 'flex',
        overflow: 'auto',
        flexDirection: 'column',
    },  
    
    fixedHeight: {
        height: 240,
    },
}));

function DashInfo(){
    const classes = useStyles();
    const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);
    return (
    <React.Fragment>
        <CssBaseline/>
        <Grid container spacing={3}>
            <Grid item xs={12} md={8} lg={9}>
                <Paper className={fixedHeightPaper}>
                    <Chart />
                </Paper>
            </Grid>
            {/* Recent Deposits */}
            <Grid item xs={12} md={4} lg={3}>
                <Paper className={fixedHeightPaper}>
                    <Deposits />
                </Paper>
            </Grid>
            {/* Recent Orders */}
            <Grid item xs={12}>
                <Paper className={classes.paper}>
                    <Orders />
                </Paper>
            </Grid>
        </Grid>
    </React.Fragment>);
}


export { DashInfo }; 