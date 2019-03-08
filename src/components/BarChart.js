import React from 'react';
import PropTypes from 'prop-types';
import { VictoryAxis, VictoryBar, VictoryChart, VictoryTheme, VictoryTooltip } from 'victory';
import colorByLevel from '../utils/colorByLevel';

const BarChart = ({ data, groupBy, field }) => {
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
            fill: (d) => colorByLevel(d[groupBy]),
            fillOpacity: 0.85
          }
        }}
        data={data}
        x={groupBy}
        y={field}
        labels={(d) => `${d[field]}`}
        labelComponent={<VictoryTooltip/>}
      />
    </VictoryChart>
  );
};

BarChart.propTypes = {
  data: PropTypes.array,
  field: PropTypes.string,
  groupBy: PropTypes.string
};

export default BarChart;
