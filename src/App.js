import "./App.css";
import certificates from "./assets/certificates.json";
import industry_content from "./assets/industry_content.json";

function App() {
  return (
    <div className="App">
      {/* <h1>Coursera Career Certificates</h1>
      <div className="certificate-container">
        {certificates.map((certificate) => {
          return (
            <div className="certificate">
              <h3>{certificate.name}</h3>
              <p>{certificate.provider}</p>
              <p>{certificate.industry}</p>
              <p>{certificate.description}</p>
              <p>{certificate.level}</p>
            </div>
          );
        })}
      </div> */}
      <h1>Industry Content</h1>
      <div className="industry-container">
        {industry_content.map((industry) => {
          return (
            <div className="industry">
              <h3>{industry.course}</h3>
              <p>{industry.partner}</p>
              <p>{industry.difficulty}</p>
              <p>{industry.career}</p>
              <p>{industry.domain}</p>
              <p>{industry.description}</p>
              <a href={industry.url}>Link</a>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;
