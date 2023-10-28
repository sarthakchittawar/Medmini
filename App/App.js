import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import TextInputComponent from './TextInputComponent'; // Replace with the actual path

const App = () => {
  return (
    <View style={styles.container}>
      <TextInputComponent />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor:"black",
    color:"white",
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
