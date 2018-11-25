Plotly.d3.csv('static/res/tsne_projections.csv', function(err, rows){
      function unpack(rows, key) {
          return rows.map(function(row)
          { return row[key]; });
      }
var true_non_suspicious = {
  x:unpack(rows, 'x1'),  y: unpack(rows, 'y1'), z: unpack(rows, 'z1'),
  mode: 'markers',
  marker: {
    size: 12,
    opacity: 0.8
  },
  type: 'scatter3d',
  name: 'True Not Suspicious'
};
var true_suspicious = {
  x:unpack(rows, 'x2'),  y: unpack(rows, 'y2'), z: unpack(rows, 'z2'),
  mode: 'markers',
  marker: {
    color: 'rgb(0, 255, 0)',
    size: 12,
    symbol: 'circle',
    line: {
      color: 'rgb(204, 204, 204)',
      width: 1
    },
    opacity: 0.8
  },
  type: 'scatter3d',
  name: 'True Suspicious'
};
var pred_suspicious = {
  x:unpack(rows, 'x3'),  y: unpack(rows, 'y3'), z: unpack(rows, 'z3'),
  mode: 'markers',
  marker: {
    color: 'rgb(255, 0, 0)',
    size: 12,
    symbol: 'circle',
  },
  type: 'scatter3d',
  name: 'Predicted Suspicious'
};
var data = [true_non_suspicious, true_suspicious, pred_suspicious];
var layout = {
      legend: {
        x: 1,
        y: 0.5
      },
      dragmode: true,
      margin: {
        l: 0,
        r: 0,
        b: 0,
        t: 0
  }};
Plotly.newPlot('myDiv', data, layout);
});