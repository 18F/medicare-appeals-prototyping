import React from 'react';
import PropTypes from 'prop-types';
import { VictoryAxis, VictoryBar, VictoryChart, VictoryTheme, VictoryTooltip } from 'victory';
import colorByLevel from '../utils/colorByLevel';

const initialState = [
  {level: 1, receipts: 13021},
  {level: 2, receipts: 8305},
  {level: 3, receipts: 6780},
  {level: 4, receipts: 4422}
];

const BarChart = ({ data }) => {
  return (
    <VictoryChart
      domainPadding={20}
      theme={VictoryTheme.material}
    >
      <VictoryAxis
        tickValues={[1, 2, 3, 4]}
        tickFormat={["Level 1", "Level 2", "Level 3", "Level 4"]}
      />
      <VictoryAxis
        dependentAxis
        tickFormat={(y) => (`${y / 1000}k`)}
      />
      <VictoryBar
        style={{
          data: {
            fill: (d) => colorByLevel(d.level),
            fillOpacity: 0.85
          }
        }}
        data={data}
        x="level"
        y="receipts"
        labels={(d) => `${d.receipts}`}
        labelComponent={<VictoryTooltip/>}
      />
    </VictoryChart>
  );
};

BarChart.propTypes = {
  data: PropTypes.array
};

BarChart.defaultProps = {
  data: initialState
};

export default BarChart;
