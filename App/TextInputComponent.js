import React, { useEffect, useState } from 'react';
import { View, TextInput, Text, StyleSheet, Dimensions } from 'react-native';
import * as Device from 'expo-device';
import axios from 'axios';

const TextInputComponent = () => {
  const [text, setText] = useState('');
  const [ansText, setAnsText] = useState('Nope');
  const [waitFlag, setFlag] = useState(true);
  const [myRAM, changeRAM] = useState(0);

  const handleTextChange = (inputText) => {
    setText(inputText);
  };

  const handleTextSubmit = async() => {
    try {
      console.log(myRAM, text)
      url = "http://192.168.196.219:5000/query"
      const headers = {
        'Content-Type': 'application/json', // Set the content type as needed
      };
  
      // Define your request body
      const requestBody = {
        "question": text,
        "RAM": myRAM
      };

      setFlag(false);

      const response = await axios.post(url, requestBody, { headers });

      // Handle the data from the response
      const posts = response.data;
      console.log('Fetched Answer:', posts);
      setAnsText(posts)
    } catch (error) {
      console.error('API Error:', error);
    }
  }

  useEffect(()=>{
    // Get RAM information
    changeRAM(Device.totalMemory);
  },[])

  useEffect(()=>{
    setFlag(true);
  },[ansText])

  // console.log("Here");

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
        editable={waitFlag}
        placeholder="Type something..."
        returnKeyType="done" // This changes the return key on the keyboard to "Done"
      />
      <Text style={styles.text}>Received Answer: {ansText}</Text>
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
