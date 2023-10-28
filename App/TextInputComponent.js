import React, { useState } from 'react';
import { View, TextInput, Text, StyleSheet, Dimensions } from 'react-native';

const TextInputComponent = () => {
  const [text, setText] = useState('');
  const [subText, setSubText] = useState('');

  const handleTextChange = (inputText) => {
    setText(inputText);
  };

  const handleTextSubmit = () => {
    setSubText(text);
  }

  const { width } = Dimensions.get('window');
  const inputWidth = 0.75 * width; 

  return (
    <View style={styles.container}>
      {/* <Text style={styles.title}>Input Text:</Text> */}
      <TextInput
        style={[styles.input, {width:inputWidth}]}
        onChangeText={handleTextChange}
        onEndEditing={handleTextSubmit} // This event is triggered when "Enter" is pressed
        value={text}
        placeholder="Type something..."
        returnKeyType="done" // This changes the return key on the keyboard to "Done"
      />
      <Text style={styles.text}>You typed: {subText}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'black',
  },
  title: {
    color: 'white',
    marginBottom: 10,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    color: 'white',
    paddingLeft: 10, // Add left padding for better alignment
    borderRadius:15
  },
  text: {
    color: 'white',
  },
});

export default TextInputComponent;
