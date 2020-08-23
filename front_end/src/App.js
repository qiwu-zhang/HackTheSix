import React from 'react';
import Signlog from "./Components/Signlog";
import Dashboard from "./Components/dashboard/Dashboard";
import {BrowserRouter as Router, Route, Link, Switch} from "react-router-dom";
function App() {
  return(
    <Router>
      <Switch>
        <Route path="/"><Signlog/></Route>
        <Route path="/dashboard"><Dashboard/></Route>
      </Switch>
    </Router>
  );
}

export default App;
