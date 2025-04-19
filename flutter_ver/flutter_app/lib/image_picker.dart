import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'image_viewer.dart';
import 'package:logging/logging.dart';

final _logger = Logger('ImagePicker');

class ImagePickerScreen extends StatefulWidget {
  const ImagePickerScreen({Key? key}) : super(key: key);

  @override
  ImagePickerScreenState createState() => ImagePickerScreenState();
}

class ImagePickerScreenState extends State<ImagePickerScreen> {
  File? _image;
  String _mode = 'object';
  final picker = ImagePicker();

  Future<void> _pickImage() async {
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);
    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
      } else {
        _logger.warning('No image selected');
      }
    });
  }

  Future<Map<String, dynamic>?> _processImage() async {
    if (_image == null) return null;

    var request = http.MultipartRequest(
      'POST',
      Uri.parse('http://localhost:8000/detect')
    );
    request.fields['mode'] = _mode;
    request.files.add(await http.MultipartFile.fromPath('file', _image!.path));

    var response = await request.send();

    if (response.statusCode == 200) {
      var responseData = await response.stream.bytesToString();
      return json.decode(responseData);
    } else {
      _logger.warning('Failed to upload image');
      return null;
    }
  }

  Future<void> _handleImage() async {
    final response = await _processImage();
    if (!mounted || response == null || _image == null) return;

    File processedImage = File(response['output_path']);
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ImageViewerScreen(
          originalImage: _image!,
          processedImage: processedImage,
          keypoints: _mode == 'pose' ? response['keypoints'] ?? [] : [],
          mode: _mode,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('WebYOLO')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _image == null
                ? const Text('No image selected.')
                : Image.file(_image!, height: 200),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text('Detection Mode:'),
                const SizedBox(width: 10),
                DropdownButton<String>(
                  value: _mode,
                  items: const [
                    DropdownMenuItem(
                      value: 'object',
                      child: Text('Object Detection'),
                    ),
                    DropdownMenuItem(
                      value: 'pose',
                      child: Text('Pose Detection'),
                    ),
                  ],
                  onChanged: (value) {
                    setState(() {
                      _mode = value!;
                    });
                  },
                ),
              ],
            ),

            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _pickImage,
              child: const Text('Pick Image'),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _handleImage,
              child: Text('Upload and ${_mode == 'object' ? 'Detect Objects' : 'Detect Pose'}'),
            ),
          ],
        ),
      ),
    );
  }
}
