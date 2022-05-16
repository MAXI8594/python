<?php
class Template {
  public $templateFile = '/tmp/template';
  public $text = '<p>Hello %s</p>';
  
  public function __construct($data = null) {
    $data = $this->readData($data);
    $this->writeData($data);
  }

  public function readData($data) {
    if (substr($data, 0, 2) !== 'O:'
    && !preg_match('/O:\d:\/', $data)) {
      return unserialize($data);
    }
    return [];
  }

  public function createBackup($file = null, $tpl = null) {
    $file = $file ?? $this->templateFile;
    $tpl = $tpl ?? $this->text;
    file_put_contents($file, $tpl);
  }

  public function writeData($data) {
    echo sprintf($this->text, htmlspecialchars($data['name']));
  }
  public function __destruct() {
    $this->createBackup();
  }