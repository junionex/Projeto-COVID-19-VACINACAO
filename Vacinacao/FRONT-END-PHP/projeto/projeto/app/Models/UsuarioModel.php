<?php namespace App\Models;
use CodeIgniter\Model;

class UsuarioModel extends Model {
protected $table = 'usuarios';
protected $primaryKey = 'id';

protected $returnType = 'array';
protected $allowedFields = ['nome', 'email', 'senha'];
protected $useTimestamps = false;
}