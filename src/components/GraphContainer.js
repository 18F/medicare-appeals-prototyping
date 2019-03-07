import React from 'react';
import GraphSelector from './GraphSelector';

const graphContainer = (GraphComponent, selectData) => {
  return class extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        data: this.props.data,
        view: 'graph'
      }
    }

    render() {
      return (
        <div className="ds-l-col--12 ds-u-padding-1">
          <GraphSelector />
          <div className="ds-l-row">
            <GraphComponent data={this.state.data} {...this.props} />
          </div>
        </div>
      );
    }
  }
}

export default graphContainer;
