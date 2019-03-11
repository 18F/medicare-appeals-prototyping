import React from 'react';
import PropTypes from 'prop-types';
import SelectView from './SelectView';

const columnContainer = (ColumnComponent, selector) => {
  class WrapperComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        filter: this.props.filter
      };

      this.updateSelect = this.updateSelect.bind(this);
    }

    updateSelect(selected, name) {
      const setState = this.setState.bind(this);
      const { options, title } = this.state[name];

      setState({[name]: { options, selected, title }})
    }

    render() {
      const { data, ...props} = this.props;

      const selectedData = selector.selectData(
        data,
        props,
        this.state.filter
      )

      return (
        <div className="ds-l-col--12">
          <div className="ds-l-row ds-u-justify-content--end">
            <SelectView
              {...this.state.filter}
              name={'filter'}
              setState={this.updateSelect}
            />
          </div>
          <ColumnComponent
            {...props}
            data={selectedData}
          />
        </div>
      );
    }
  }

  WrapperComponent.propTypes = {
    category: PropTypes.string.isRequired,
    data: PropTypes.array.isRequired,
    difference: PropTypes.string,
    field: PropTypes.string,
    filter: PropTypes.object.isRequired,
    groupBy: PropTypes.string.isRequired,
    label: PropTypes.string.isRequired,
    minuend: PropTypes.string,
    subtrahend: PropTypes.string
  }

  return WrapperComponent
}

export default columnContainer;
