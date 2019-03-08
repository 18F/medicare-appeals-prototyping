import React from 'react';
import PropTypes from 'prop-types';
import { VictoryAxis, VictoryBar, VictoryChart, VictoryTheme, VictoryTooltip } from 'victory';
import colorByLevel from '../utils/colorByLevel';

const BarChart = ({ data, groupBy, field, height, maxDomain }) => {
  return (
    <VictoryChart
      domainPadding={15}
      theme={VictoryTheme.material}
      maxDomain={{y: maxDomain}}
      animate={{ duration: 300, easing: "poly" }}
      height={height}
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
            fillOpacity: 0.8
          }
        }}
        data={data}
        x={groupBy}
        y={field}
        labels={(d) => `${d[field]}`}
        labelComponent={<VictoryTooltip cornerRadius={0} flyoutStyle={{fill: "white"}}/>}
      />
    </VictoryChart>
  );
};

BarChart.propTypes = {
  data: PropTypes.array,
  field: PropTypes.string,
  groupBy: PropTypes.string,
  height: PropTypes.number,
  maxDomain: PropTypes.number
};

BarChart.defaultProps = {
  height: 230
};

export default BarChart;
