import {useRef, useState} from "react";
import axios from "axios";


const BASE_API_URL = "http://localhost/api"
const PREDICTION_API = BASE_API_URL+"/prediction"



function App() {
    const [prediction, setPrediction] = useState(null);
    const query = useRef("");

    const handleQuery = (query)=>{
        axios.get(PREDICTION_API,
            {
                params: {
                    query: query.current.value
                 }
            }
        ).then(r => {
            setPrediction(r.data);
        })
    };





  return (
    <div className="container">
      <div className="row justify-content-center">
        <div className="col col-auto w-50">
            <div className="d-flex flex-column align-items-center">
                <h6 className="text-center">Type text. And i will analyze it.)</h6>
                <textarea className="w-100" ref={query} rows={6} cols={10}>
                </textarea>
                <button className="btn btn-info my-1" onClick={()=>handleQuery(query)}>submit</button>
            </div>
                {prediction !== null &&
                    <div className="">
                        <p>Label: {prediction.label}</p>
                        <p>Score: {prediction.score}</p>
                        <p>Elapsed Time: {prediction.elapsed_time}</p>
                    </div>
                }
        </div>
      </div>
    </div>
  );
}

export default App;
