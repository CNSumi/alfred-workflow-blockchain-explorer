#!/usr/bin/env php
<?php

$dir = dirname(__DIR__);

print "Building workflow in $dir\n";

$version = "1.0.0";

$plist = $dir.'/info.plist';

exec(sprintf('/usr/libexec/PlistBuddy -c "Set :version %s" %s', $version, escapeshellarg($plist)));

$zipFile = $dir.'/bc.zip';
if (file_exists($zipFile)) {
    unlink($zipFile);
}

$zip = new PharData($zipFile);

$files = [
    'main.py',
    'icon.png',
    'info.plist'
];

foreach ($files as $file) {
    $zip->addFile($dir.'/'.$file, $file);
}
foreach (glob($dir.'/icons/*.png') as $path) {
    $zip->addFile($path, 'icons/'.basename($path));
}

$zip->compressFiles(Phar::GZ);

$workflow = $dir.'/bc.alfredworkflow';
if (file_exists($workflow)) {
    unlink($workflow);
}
rename($zipFile, $workflow);
