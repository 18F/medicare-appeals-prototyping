import React from 'react';
import PropTypes from 'prop-types';
import SelectView from './SelectView';

const graphContainer = (GraphComponent, selectData) => {
  class WrapperComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        filter: this.props.filter,
        view: 'graph',
        viewOptions: ['graph', 'table'],
        viewTitle: 'Select View'
      };

      this.updateFilter = this.updateFilter.bind(this);
      this.updateContainerView = this.updateContainerView.bind(this);
    }

    updateFilter(selected) {
      const setState = this.setState.bind(this);
      const { options, title } = this.state.filter;

      setState({filter: { options, selected, title }})
    }

    updateContainerView(val) {
      const setState = this.setState.bind(this);
      setState({view: val});
    }

    render() {
      const { data, ...props} = this.props;

      const selectedData = selectData(
        data,
        this.props.groupBy,
        this.props.field,
        this.props.category,
        this.state.filter
      )

      return (
        <div className="ds-l-col--12 ds-u-padding-1">
          <div className="ds-l-row ds-u-justify-content--end">
            <SelectView
              disabled
              options={this.state.viewOptions}
              selected={this.state.view}
              title={this.state.viewTitle}
              setState={this.updateContainerView}
            />
            <SelectView
              {...this.state.filter}
              setState={this.updateFilter}
            />
          </div>
          <div className="ds-l-row">
            <GraphComponent data={selectedData} {...props}/>
          </div>
        </div>
      );
    }
  }

  WrapperComponent.propTypes = {
    data: PropTypes.array,
    filter: PropTypes.object,
    groupBy: PropTypes.string,
    category: PropTypes.string,
    field: PropTypes.string
  }

  WrapperComponent.defaultProps = {
    filter: {
      options: ['all', 'non-rac', 'rac'],
      selected: 'all',
      title: 'Filter values'
    },
    groupBy: 'level',
    category: 'denial_category',
    field: 'receipts'
  }

  return WrapperComponent
}

export default graphContainer;
