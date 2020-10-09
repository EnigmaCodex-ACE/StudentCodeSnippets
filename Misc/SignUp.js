import React, {Component} from 'react';
import {
  Text,
  View,
  StyleSheet,
  Image,
  ScrollView,
  FlatList,
} from 'react-native';
type Props = {};
export default class SignUp extends Component<Props> {
  render() {
    return (
      <View style={styles.container}>
        <Text
          style={{fontSize: 30, borderWidth: 2, borderRadius: 5}}
          onPress={() => {
            this.props.navigation.navigate('Login');
          }}>
          SignUp
        </Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});
