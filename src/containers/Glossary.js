import React from 'react';
import {
  Card,
  IconButton,
  Pane,
  SideSheet
} from 'evergreen-ui';

const Glossary = () => {
  class GlossaryComponent extends React.Component {
    constructor(props) {
      super(props);

      this.state = {
        isShown: false
      }

      this.setState = this.setState.bind(this);
    }

    render() {
      const setState = this.setState;

      return (
        <React.Fragment>
          <SideSheet
            isShown={this.state.isShown}
            onCloseComplete={() => setState({ isShown: false })}
            containerProps={{
              display: 'flex',
              flex: '1',
              flexDirection: 'column',
            }}
            preventBodyScrolling={true}
            width="200"
          >
            <Pane zIndex={1} flexShrink={0} elevation={0} backgroundColor="white">
              <Pane
                padding={16}
                display="flex"
                alignItems="center"
                justifyContent="flex-end"
              >
                <div className="show-small">
                  <IconButton
                    icon="cross"
                    appearance="minimal"
                    onClick={() => setState({ isShown: false })}
                  />
                </div>
              </Pane>
              <Pane padding={16}>
                <h1 className="ds-title">Glossary</h1>
                <p className="ds-u-color--muted ds-u-font-size--small ds-u-margin--0">
                  This glossary of terms to help describe the different terms used within the dashboard.
                </p>
              </Pane>
            </Pane>
            <Pane flex="1" overflowY="scroll" background="tint1" padding={16}>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Appeal
                  </h3>
                  <div>
                    The process used when a party to dispute a determination on claims.
                  </div>
                </div>
              </Card>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Appellant
                  </h3>
                  <div>An appellant is the identified entity that is related to an appeal</div>
                </div>
              </Card>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Attorney Adjudicator
                  </h3>
                  <div>
                    A licensed attorney employed by HHS with knowledge of Medicare laws
                  </div>
                </div>
              </Card>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Claim
                  </h3>
                  <div>
                    An Medicare claims which has been denied and is now being appealed
                  </div>
                </div>
              </Card>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Disposition or Determination
                  </h3>
                  <div>
                    A decision made on payment and/or liability of a claim/s in an appeal
                  </div>
                </div>
              </Card>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Holistic Appeal
                  </h3>
                  <div>
                    A series of interconnected appeals that represent the entire lifecycle of an
                    appellant's claims.
                  </div>
                </div>
              </Card>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Provider
                  </h3>
                  <div>
                    An entity that is approved to provide medical services to Medicare beneficiaries.
                  </div>
                </div>
              </Card>
              <Card
                backgroundColor="white"
                padding={16}
                margin={16}
                elevation={0}
                display="flex"
              >
                <div className="ds-u-margin-right--2">
                  <h3 className="ds-text">
                    Receipt
                  </h3>
                  <div>
                    An appeal that has been received by one of the levels
                  </div>
                </div>
              </Card>
            </Pane>
          </SideSheet>
          <button
            className="ds-c-button ds-c-button--small ds-c-button--primary"
            onClick={() => setState({ isShown: true })}
          >
            Glossary
          </button>
        </React.Fragment>
      );
    }
  }

  return <GlossaryComponent />
}

export default Glossary;
